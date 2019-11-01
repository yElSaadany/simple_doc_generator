from docstring_parser import parse
from markdown import Markdown, MarkdownSection


def create_doc_file(markdown, name):
    markdown.generate(name)


def generate_markdown(docstrings, title):
    sections = []
    is_method = False
    for signature, docstring in docstrings.items():
        if "class" in signature:
            is_method = False
        section = MarkdownSection(signature, is_method)
        docstring = parse(docstring)
        section.add_line(docstring.short_description[3:])
        section.add_line(str(docstring.long_description))
        if is_method:
            section.add_line("#### Arguments")
        else:
            section.add_line("### Arguments")
        tmp = ["%s (*%s*): %s" % (arg.arg_name, arg.type_name,
                                  arg.description)
               for arg in docstring.params]
        section.add_list(tmp)

        if "class" in signature:
            is_method = True

        if docstring.returns:
            section.add_line("### Returns")
            section.add_line(docstring.returns.description[:-4])

        sections.append(section)

    ret = Markdown(title)
    ret.sections = sections
    return ret
