import os
import argparse

def check_files(input_file, output_file):
    if not os.path.isfile(input_file):
        print("Error: %s does not exist" % input_file)
        exit(2)

    if os.path.isfile(output_file):
        warning = input("Warning: %s already exists. Proceed? (Y/n)"%(
            output_file))
        if warning == 'N' or warning == 'n':
            exit(0)

def init_args():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", metavar="path",
                       required=True, help="path to input file")
    parse.add_argument("-o", metavar="path",
                       required=True, help="path to output file")
    return parse.parse_args()
