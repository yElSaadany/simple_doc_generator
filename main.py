import generator as gen
from utils.arguments import init_args, check_files
from extractor import extract_docstring_from_indexes


def main(args):
    input_file = args.i
    output_file = args.o
    name = input("Name of your project: ")
    docstrings = extract_docstring_from_indexes(input_file)
    res = gen.generate_markdown(docstrings, name)
    gen.create_doc_file(res, output_file)


if __name__ == '__main__':
    args = init_args()
    check_files(args.i, args.o)
    main(args)
