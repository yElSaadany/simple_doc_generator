import simpledoc.generator as gen
from simpledoc.utils.arguments import init_args, check_files
from simpledoc.extractor import extract_docstrings
import os
import sys


def main():
    args = init_args()
    check_files(args.i, args.o)
    if len(args.i.split('/')) > 1:
        current_dir = os.getcwd()
        os.chdir('/'.join(args.i.split('/')[:-1]))
    module = args.i.split('/')[-1][:-3]
    output_file = args.o
    sys.path.append('')
    docstrings = extract_docstrings(module)
    os.chdir(current_dir)
    res = gen.generate_markdown2(docstrings)
    gen.create_doc_file(res, output_file)
