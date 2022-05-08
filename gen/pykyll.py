import mistletoe
import argparse
import json


def parse_markdown(mdfile):
    with open(mdfile, "r") as fp:
        lines = fp.readlines()
    # read the '---' preamble region of the markdown files and after reading
    # those, delete them before passing the markdown content to the mistletoe
    # parser+renderer
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
    # content to the mistletoe for parsing
    if preamble == 2:
        lines = lines[i:]
    content = mistletoe.markdown(''.join(lines))
    return page_cfg, content


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
        page_cfg, content = parse_markdown(args.md)
    return


if __name__ == "__main__":
    main()
