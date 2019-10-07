import generator as gen
import sys, getopt
import os


def main(argv):
    input_file = None
    output_file = None
    for i in range(len(argv)):
        if argv[i] == '-i':
            input_file = argv[i+1]
        elif argv[i] == '-o':
            output_file = argv[i+1]
    if input_file is None or output_file is None:
        print('options: -i <input_file> -o <output_file>')
        exit(2)

    if not os.path.isfile(input_file):
        print("Error: %s does not exist" % input_file)
        exit(2)

    res = gen.extract_docstring(input_file)
    gen.create_file(gen.generate_markdown(res), output_file)

if __name__ == '__main__':
    main(sys.argv)
