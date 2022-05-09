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


def length(arr):
    return len(arr)


def parse_markdown(mdfile, args, content=""):
    page_cfg, lines = parse_preamble(mdfile)
    next_content = mistletoe.markdown(lines)
    if "layout" in page_cfg:
        next_file = args.cfg["dirs"]["layouts"] + "/" + page_cfg["layout"] + ".html"
        text = parse_markdown(next_file, args, content=next_content)
    else:
        text = next_content
    loader = jinja2.FileSystemLoader(args.cfg["dirs"]["layouts"])
    environment = jinja2.Environment(loader=loader)
    environment.filters["relative_url"] = relative_url
    environment.filters["escape"] = escape
    environment.filters["length"] = length
    tm = environment.from_string(text)
    content = tm.render(site=args.cfg, content=content, page=page_cfg, post={})
    return content


def validateargs(args):
    if args.md is None:
        raise Exception("-md is mandatory")
    if args.html is None:
        raise Exception("-html is mandatory")


def parseargs():
    desc = "Generate jekyll-like pages but using python"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-cfg", default="config.json", type=str,
        help="Path to the global config file.")
    parser.add_argument("-html", default=None, type=str,
        help="Path to the html page for the given input markdown file.")
    parser.add_argument("-md", default=None, type=str,
        help="Path to the markdown file that needs to be converted to html.")
    args = parser.parse_args()
    validateargs(args)
    with open(args.cfg, "r") as fp:
        args.cfg = json.load(fp)
    return args


def main():
    args = parseargs()
    if args.md and args.html:
        content = parse_markdown(args.md, args)
        print(content)
    return


if __name__ == "__main__":
    main()
