def is_signature(str):
    """Check weather or not the string is a class or function signature"""
    if "class" in str or "def" in str:
        return str
    return False


def get_signatures_indexes(file):
    """Reads a file and outputs the indexes of every signature.
    
    This function is used to get the first and last docstrings declarations for every class or method/function.

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
