import generator as gen
import sys, argparse
from utils.arguments import init_args, check_files

def main(args):
    input_file = args.i
    output_file = args.o
    res = gen.extract_docstring(input_file)
    gen.create_file(gen.generate_markdown(res), output_file)

if __name__ == '__main__':
    args = init_args()
    check_files(args.i, args.o)
    main(args)
