import os
import argparse


def check_files(input_file):
    """Checks if arguments are valid.

    Args:
        input_file (str): File for which you want to generate documentation.
        output_file (str): Markdown file outputed by the program.

    Returns:
        Nothing, only exit with error message if something is wrong.
    """
    if not os.path.exists(input_file):
        print("Error: %s does not exist" % input_file)
        exit(2)


def init_args():
    """Initializes arguments passed to the program.

    Uses argparse to get user's argument from the command line.

    Returns:
        Parsed arguments in objects named after them.
    """
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", metavar="path", required=True, help="path to input file")
    parse.add_argument("-v", help="verbose mode, for debug", action="store_true")
    return parse.parse_args()
