import mistletoe
import argparse
import json
import jinja2
import os
import re
import subprocess
import glob


POST_DATE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-")


def parse_preamble(file):
    with open(file, "r") as fp:
        lines = fp.readlines()
    # read the '---' preamble region of the markdown files and after reading
    # those, delete them before passing the markdown content to the mistletoe
    # parser+renderer or the template string for jinja2 to expand
    preamble = 0
    page_cfg = {}
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("---"):
            preamble = preamble + 1
            if preamble == 1:
                continue
            elif preamble == 2:
                i = i + 1
                break
        if preamble == 1:
            if line.startswith("#"):  # comment
                continue
            kv = line.split(": ", 1)
            key = kv[0]
            val = kv[1]
            if key == "tags":
                val = val.split(" ")
            elif key == "needmath":
                val = True if val == "true" else False
            page_cfg[key] = val
    # this means a preamble was found and `page_cfg` was parsed successfully,
    # which means we should delete the preamble before passing the rest of the
    # content to the mistletoe/jinja2 for parsing
    if preamble == 2:
        lines = lines[i:]
    lines = ''.join(lines)
    return page_cfg, lines


# TODO!
def relative_url(url):
    return url


# TODO!
def escape(text):
    return text


# TODO!
def date_to_xmlschema(text):
    return text


def length(arr):
    return len(arr)


def post_date(filename):
    base = os.path.basename(filename)
    grp = re.search(POST_DATE, base)
    if not grp:
        raise Exception(f"Post {filename} does not have date prefix!")
    return "%s-%s-%s" % (grp.group(1), grp.group(2), grp.group(3))


def post_last_modified(mdfile):
    out = subprocess.check_output("git log -1 --date=format:'%%Y-%%m-%%d' --format='%%ad' %s" % mdfile, shell=True)
    out = out.strip()
    return out.decode("ascii")


def post_url(filename, site, is_post):
    base = os.path.basename(filename)
    base = base.replace(".md", ".html")  # TODO: use "extension" keyword!
    base = base.replace(".markdown", ".html")
    return os.path.join(site["dirs"]["html"],
                        site["dirs"]["posts"] if is_post else "",
                        base)


def get_tmpl(args, text):
    loader = jinja2.FileSystemLoader(os.path.join(args.cfg["dirs"]["main"],
                                                  args.cfg["dirs"]["layouts"]))
    environment = jinja2.Environment(loader=loader)
    environment.filters["relative_url"] = relative_url
    environment.filters["escape"] = escape
    environment.filters["length"] = length
    environment.filters["date_to_xmlschema"] = date_to_xmlschema
    return environment.from_string(text)


def parse_template(tmplfile, args, content, prev_cfg):
    tmp_cfg = prev_cfg.copy()
    del tmp_cfg["layout"]
    page_cfg, lines = parse_preamble(tmplfile)
    page_cfg.update(tmp_cfg)  # child's preamble gets higher priority
    tm = get_tmpl(args, lines)
    content = tm.render(site=args.cfg, content=content, page=page_cfg)
    if "layout" in page_cfg:
        next_file = os.path.join(args.cfg["dirs"]["main"],
                                 args.cfg["dirs"]["layouts"],
                                 page_cfg["layout"] + ".html")
        content = parse_template(next_file, args, content, page_cfg)
    return content


def parse_markdown(mdfile, args, is_post=False):
    post = {}
    if is_post:
        post["date"] = post_date(mdfile)
    post["url"] = post_url(mdfile, args.cfg, is_post)
    if not args.regen:
        md_time = os.path.getmtime(mdfile)
        html_time = os.path.getmtime(post["url"]) if os.path.exists(post["url"]) else 0
        if md_time < html_time:
            return
    post["last_modified"] = post_last_modified(mdfile)
    print(f"Generating html for {mdfile}...")
    page_cfg, lines = parse_preamble(mdfile)
    post.update(page_cfg)
    content = mistletoe.markdown(lines)
    if "layout" in page_cfg:
        next_file = os.path.join(args.cfg["dirs"]["main"],
                                 args.cfg["dirs"]["layouts"],
                                 page_cfg["layout"] + ".html")
        content = parse_template(next_file, args, content, post)
    # collect all tags mentioned for this post
    if "tags" in post:
        for tag in post["tags"]:
            args.cfg["tags"].add(tag)
    if is_post:
        # maintain a global list of posts
        args.cfg["posts"].append(post)
        # also maintain a tags to posts mapping
        for tag in post["tags"]:
            if tag not in args.cfg["tags_to_posts"]:
                args.cfg["tags_to_posts"][tag] = []
            args.cfg["tags_to_posts"][tag].append(len(args.cfg["posts"]))
    d = os.path.dirname(post["url"])
    if not os.path.exists(d):
        os.mkdir(d)
    with open(post["url"], "w") as fp:
        fp.write(content)
    return


def generate_html(args):
    # generate all the posts first
    posts_dir = os.path.join(args.cfg["dirs"]["main"],
                             args.cfg["dirs"]["posts"],
                             "*." + args.cfg["extension"])
    for file in glob.glob(posts_dir):
        parse_markdown(file, args, True)
    # generate the final set of pages inside 'main' directory next
    main_dir = os.path.join(args.cfg["dirs"]["main"],
                            "*.md")  # TODO: use "extension" keyword!!
    for file in glob.glob(main_dir):
        parse_markdown(file, args, False)


def validateargs(args):
    pass


def parseargs():
    desc = "Generate jekyll-like pages but using python"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-cfg", default="config.json", type=str,
        help="Path to the global config file.")
    parser.add_argument("-regen", action="store_true", default=False,
        help="Forcefully regenerate all the html files")
    args = parser.parse_args()
    validateargs(args)
    with open(args.cfg, "r") as fp:
        args.cfg = json.load(fp)
        args.cfg["posts"] = []
        args.cfg["tags"] = set()
        args.cfg["tags_to_posts"] = {}
    return args


if __name__ == "__main__":
    args = parseargs()
    generate_html(args)
