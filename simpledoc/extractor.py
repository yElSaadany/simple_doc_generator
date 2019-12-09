"""Module used to extract the docstrings inside a Python file"""


def is_signature(string):
    """Check weather or not the string is a class or function signature"""
    if "class" in string or "def" in string:
        return string
    return False


def get_signatures_indexes(file):
    """Reads a file and outputs the indexes of every signature.

    This function is used to get the first and last
    docstrings declarations for every class or method/function.

    Note:
        Does not work with single-line docstring for now.

    Args:
        file (str): Path to source code file (e.g. 'example.py')

    Returns:
        A dictionnary with the file's classes/functions/methods signatures as
        keys and a tuple containing dosctrings indexes as values.


    """
    with open(file, 'r') as doc:
        lines = doc.readlines()

    ret = {}
    for i in range(len(lines)):
        if '"""' in lines[i] and is_signature(lines[i-1]):
            start = i-1
            signature = is_signature(lines[start])
        elif '"""' in lines[i] and not is_signature(lines[i-1]):
            ret[signature] = (start, i)

    print(ret)
    return ret


def extract_docstring_from_indexes(file):
    """Returns the actual docstrings of a source code file.

    Args:
        file (str): Path to source code file (e.g. 'example.py')

    Returns:
        A dictionnary containing the file's signatures as keys and their
        corresponding docstrings as values.
    """
    with open(file, 'r') as doc:
        lines = doc.readlines()

    docstrings_indexes = get_signatures_indexes(file)
    ret = {}
    for signature, (start, stop) in docstrings_indexes.items():
        ret[signature] = ''.join(lines[start+1:stop+1])

    return ret


def is_one_line_doc(string):
    string = string.strip()
    if string[:3] == string[-3:] == '"""':
        return True


def get_declarations(file):
    with open(file, 'r') as doc:
        lines = doc.readlines()

    ret = []
    for line in lines:
        line = line.strip()
        if line[:3] == "def" or line[:5] == "class":
            ret.append(line.split(' ')[1].split('(')[0])

    return ret


def extract_docstrings(module):
    declarations = get_declarations("%s.py" % module)
    print(declarations)
    module = __import__(module)

    tmp = {}
    ret = {'classes': {}, 'functions': {}}
    for key, value in module.__dict__.items():
        if key[:2] != "__" and True in [dec in key for dec in declarations]:
            tmp[key] = value

    for key, value in tmp.items():
        if type(value) == type(type):  # It's a class
            ret['classes'].update({key: {'self': value.__doc__,
                                         'methods': {}}})

            for name, method in value.__dict__.items():
                if (name[:2] != "__"
                        and True in [dec in name for dec in declarations]):
                    doc = method.__doc__
                    ret['classes'][key]['methods'].update({name: doc})
        else:  # It's a function
            ret['functions'].update({key: value.__doc__})

    return ret
