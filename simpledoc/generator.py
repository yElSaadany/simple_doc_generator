from docstring_parser import parse
from simpledoc.markdown import Markdown, MarkdownSection


def create_doc_file(markdown, name):
    """Creates a mardown file.

    Args:
        mardown (Markdown): Markdown object to be exported as a MD file
        name (str): Name of the MD file (e.g. 'documentation.md')

    Returns:
        Nothing.
    """
    markdown.generate(name)


def function_section(signature, docstring):
    """Returns a Markdown Section made for functions

    Args:
        signature (str): Function to be documented
        docstring (str): Its docstring

    Returns:
        Markdown section.
    """
    section = MarkdownSection(signature, False)
    docstring = parse(docstring)
    section.add_line(docstring.short_description[3:])
    section.add_line(str(docstring.long_description))
    section.add_line("### Arguments")
    tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                              arg.description)
           for arg in docstring.params]
    section.add_list(tmp)

    if docstring.returns:
        section.add_line("### Returns")
        section.add_line(docstring.returns.description[:-4])

    return section


def method_section(signature, docstring):
    """Same as function_section but for a method."""
    section = MarkdownSection(signature, True)
    docstring = parse(docstring)
    section.add_line(docstring.short_description[3:])
    section.add_line(str(docstring.long_description))
    section.add_line("#### Arguments")
    tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                              arg.description)
           for arg in docstring.params]
    section.add_list(tmp)

    if docstring.returns:
        section.add_line("#### Returns")
        section.add_line(docstring.returns.description[:-4])

    return section


def class_section(signature, docstring):
    """Same as function_section but for a class."""
    section = MarkdownSection(signature, False)
    docstring = parse(docstring)
    section.add_line(docstring.short_description[3:])
    section.add_line(str(docstring.long_description))
    section.add_line("### Arguments")
    tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                              arg.description)
           for arg in docstring.params]
    section.add_list(tmp)

    if docstring.returns:
        section.add_line("### Returns")
        section.add_line(docstring.returns.description[:-4])

    return section


def generate_markdown(docstrings, title):
    """Combines all the Markdown sections together to form a complete markdown.

    Args:
        docstrings (Dict): Returned by extractor.extract_doctring_from_indexes()
        title (str): Title of the Markdown document

    Returns:
        A Markdown object.
    """
    sections = []
    for signature, docstring in docstrings.items():
        if "class" in signature:
            sections.append(class_section(signature, docstring))
        elif "    " in signature:
            sections.append(method_section(signature, docstring))
        else:
            sections.append(function_section(signature, docstring))

    ret = Markdown(title)
    ret.sections = sections


    return ret
