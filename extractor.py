from docstring_parser import parse


def is_signature(str):
    if "class" in str or "def" in str:
        return str
    return False


def get_signatures_indexes(file):
    with open(file, 'r') as doc:
        lines = doc.readlines()

    ret = {}
    for i in range(len(lines)):
        if '"""' in lines[i] and is_signature(lines[i-1]):
            start = i-1
            signature = is_signature(lines[start])
        elif '"""' in lines[i] and not is_signature(lines[i-1]):
            ret[signature] = (start, i)

    return ret


def extract_docstring_from_indexes(file):
    with open(file, 'r') as doc:
        lines = doc.readlines()

    docstrings_indexes = get_signatures_indexes(file)
    ret = {}
    for signature, (start, stop) in docstrings_indexes.items():
        ret[signature] = ''.join(lines[start+1:stop+1])

    return ret
