from simpledoc.utils.debug import debug
import simpledoc.generator as gen
from simpledoc.utils.arguments import init_args, check_files
from simpledoc.extractor import extract_docstrings
import os
import sys


def main():
    args = init_args()
    check_files(args.i)
    print(args.v)
    if args.v:
        os.environ["DEBUG"] = "debug"
        debug("Verbose mode")
    else:
        args.v = False
    sys.path.append('')
    current_dir = os.getcwd()
    if len(args.i.split('/')) > 1:
        os.chdir('/'.join(args.i.split('/')[:-1]))

    markdowns = []
    if args.i.split('/')[-1][-3:] == '.py':
        module = args.i.split('/')[-1][:-3]
        docstrings = extract_docstrings(module)
        os.chdir(current_dir)
        markdowns.append(gen.generate_markdown2(docstrings))
    else:
        os.chdir(args.i)
        modules = [module for module in os.listdir() if module[-3:] == '.py']

        for module in modules:
            module = module[:-3]
            docstrings = extract_docstrings(module)
            os.chdir(current_dir)
            markdowns.append(gen.generate_markdown2(docstrings))

    if not os.path.isdir('./build'):
        os.mkdir('build')
    os.chdir('build')
    gen.create_doc_files(markdowns)
