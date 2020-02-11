import os
import sys
import argparse
from bs4 import BeautifulSoup


def vue_parse(file):
    with open(file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        # remove script tagged text
        for script in soup(["script"]):
            script.decompose()
        return soup.get_text('\n', strip=True)


def parse_args(argv):
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='vue_parser_args')
    # set the argument formats
    parser.add_argument(
        '--file', default=os.path.join('.', 'vue', 'appSafer.vue'),
        help='vue file to be parsed')

    return parser.parse_args(argv[1:])


if __name__ == '__main__':
    args = parse_args(sys.argv)
    text = vue_parse(args.file)
    print(text)
