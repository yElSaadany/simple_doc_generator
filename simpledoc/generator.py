"""Module in charge of creating the markdown file"""
from docstring_parser import parse
from simpledoc.markdown import Markdown, MarkdownSection


def create_doc_files(markdowns):
    """Creates a mardown file.

    Args:
        mardown (Markdown): Markdown object to be exported as a MD file
        name (str): Name of the MD file (e.g. 'documentation.md')

    Returns:
        Nothing.
    """
    for markdown in markdowns:
        markdown.generate(markdown.name+'.md')


def function_section(signature, docstring):
    """Returns a Markdown Section made for functions

    Args:
        signature (str): Function to be documented
        docstring (str): Its docstring

    Returns:
        Markdown section.
    """
    section = MarkdownSection(signature, False)
    section.add_line("**Function**")
    docstring = parse(docstring)
    if docstring.short_description is not None:
        section.add_line(docstring.short_description)
    if docstring.long_description is not None:
        section.add_line(str(docstring.long_description))
    if len(docstring.params) != 0:
        section.add_line("### Arguments")
        tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                                  arg.description)
               for arg in docstring.params]
        section.add_list(tmp)

    if docstring.returns:
        section.add_line("### Returns")
        section.add_line(docstring.returns.description)

    return section


def method_section(signature, docstring):
    """Same as function_section but for a method."""
    section = MarkdownSection(signature, True)
    section.add_line("**Method**")
    docstring = parse(docstring)
    if docstring.short_description is not None:
        section.add_line(docstring.short_description)
    if docstring.long_description is not None:
        section.add_line(str(docstring.long_description))
    if len(docstring.params) != 0:
        section.add_line("#### Arguments")
        tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                                  arg.description)
               for arg in docstring.params]
        section.add_list(tmp)

    if docstring.returns:
        section.add_line("#### Returns")
        section.add_line(docstring.returns.description)

    return section


def class_section(signature, docstring):
    """Same as function_section but for a class."""
    section = MarkdownSection(signature, False)
    section.add_line("**Class**")
    docstring = parse(docstring)
    section.add_line(docstring.short_description)
    if docstring.long_description is not None:
        section.add_line(str(docstring.long_description))
    if len(docstring.params) != 0:
        section.add_line("### Arguments")
        tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                                  arg.description)
               for arg in docstring.params]
        section.add_list(tmp)

    if docstring.returns:
        section.add_line("### Returns")
        section.add_line(docstring.returns.description)

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
        splitted_signature = signature.split(' ')
        method = False
        if len(splitted_signature) >= 4:
            if splitted_signature[:4] == ['', '', '', '']:
                declaration = splitted_signature[4]
                method = True
                signature = ''.join(splitted_signature[5:])
            else:
                declaration = splitted_signature[0]
                signature = ''.join(splitted_signature[1:])
        else:
            declaration = splitted_signature[0]
            signature = ''.join(splitted_signature[1:])

        if declaration == "class":
            sections.append(class_section(signature, docstring))
        elif method:
            sections.append(method_section(signature, docstring))
        else:
            sections.append(function_section(signature, docstring))

    ret = Markdown(title)
    ret.sections = sections

    return ret


def generate_markdown2(docstrings):
    title = list(docstrings.keys())[0]
    sections = []
    print(docstrings)
    for name, docstring in docstrings['functions'].items():
        print("maisie")
        print(name)
        print(docstring)
        sections.append(function_section(name, docstring))

    for name, docstring in docstrings['classes'].items():
        sections.append(class_section(name, docstring['self']))
        for method, met_doc in docstring['methods'].items():
            print(method)
            sections.append(method_section(method, met_doc))

    ret = Markdown(title)
    #ret.add_content(docstrings[title])
    ret.sections = sections

    return ret
