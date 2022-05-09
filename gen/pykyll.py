import mistletoe
import argparse
import json
import jinja2


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


def get_tmpl(args, text):
    loader = jinja2.FileSystemLoader(args.cfg["dirs"]["layouts"])
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
        next_file = args.cfg["dirs"]["layouts"] + "/" + page_cfg["layout"] + ".html"
        content = parse_template(next_file, args, content, page_cfg)
    return content


def parse_markdown(mdfile, args, is_post=False):
    page_cfg, lines = parse_preamble(mdfile)
    content = mistletoe.markdown(lines)
    if "layout" in page_cfg:
        next_file = args.cfg["dirs"]["layouts"] + "/" + page_cfg["layout"] + ".html"
        content = parse_template(next_file, args, content, page_cfg)
    if is_post:
        post = page_cfg
        post["date"] = "-NA-"  # TODO!
        post["url"] = "-NA-"   # TODO!
        if "tags" in post:
            for tag in post["tags"]:
                args.cfg["tags"].add(tag)
        args.cfg["posts"].append(post)
    return content


def validateargs(args):
    if args.md is None:
        raise Exception("-md is mandatory")


def parseargs():
    desc = "Generate jekyll-like pages but using python"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-cfg", default="config.json", type=str,
        help="Path to the global config file.")
    parser.add_argument("-md", default=None, type=str,
        help="Path to the markdown file that needs to be converted to html.")
    args = parser.parse_args()
    validateargs(args)
    with open(args.cfg, "r") as fp:
        args.cfg = json.load(fp)
        args.cfg["posts"] = []
        args.cfg["tags"] = set()
    return args


def main():
    args = parseargs()
    if args.md:
        content = parse_markdown(args.md, args, is_post=True)
        print(content)
    return


if __name__ == "__main__":
    main()
