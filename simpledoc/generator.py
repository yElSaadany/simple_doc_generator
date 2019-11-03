from docstring_parser import parse
from markdown import Markdown, MarkdownSection


def create_doc_file(markdown, name):
    markdown.generate(name)


def function_section(signature, docstring):
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
    sections = []
    for signature, docstring in docstrings.items():
        print("    " in signature)
        if "class" in signature:
            sections.append(class_section(signature, docstring))
        elif "    " in signature:
            sections.append(method_section(signature, docstring))
        else:
            sections.append(function_section(signature, docstring))

    ret = Markdown(title)
    ret.sections = sections


    return ret
