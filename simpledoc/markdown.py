class Markdown():
    """Represents a markdown file
    """
    def __init__(self, title):
        self.title = "# " + title + '\n'
        self.content = ""
        self.sections = []

    def add_content(self, text):
        self.content += text

    def add_section(self, section):
        self.sections.append(section)

    def process_sections(self):
        for section in self.sections:
            self.content += section.generate()

    def generate(self, name):
        self.process_sections()
        with open(name, 'w') as doc:
            doc.write(self.title)
            doc.write(self.content)


class MarkdownSection():
    """Represents a section in a markdown file
    """
    def __init__(self, title, subsection=False):
        if subsection:
            self.title = "### " + title + '\n'
        else:
            self.title = "## " + title + '\n'
        self.content = ""

    def add_content(self, text):
        self.content += text

    def add_line(self, line):
        """Adds a line to section's content.

        Takes whatever line markdown line you give it and adds
        a NEWLINE to it.

        Args:
            line (str): Line you want to add.

        Returns:
            Nothing, inplace operation.
        """
        self.content += line + '\n\n'

    def add_list(self, items):
        """Adds a markdown list to the section.

        Args:
            items (List): Strings of the items you want to list.

        Returns:
            Nothing, inplace operation.
        """
        md = ""
        for item in items:
            md += "* " + item + '\n'

        self.content += md

    def generate(self):
        return self.title + self.content
