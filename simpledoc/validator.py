"""Module used to validate docstrings"""
from docstring_parser import parse


def validate(text):
    """Do the actual validation

    This function will tell what you docstring lacks.

    Note:
        A missing part can be normal, for example a function
        with no parameter or no return. (todo)

    Args:
        text (str): Docstring to be validated.

    Returns:
        A list with the names of missing parts of docstrings.
    """
    missing = []
    docstring = parse(text)

    if docstring.short_description is None:
        missing.append("short_description")
    if docstring.long_description is None:
        missing.append("long_description")
    if len(docstring.params) == 0:
        missing.append("parameters")
    if docstring.returns is None:
        missing.append("returns")

    return missing
