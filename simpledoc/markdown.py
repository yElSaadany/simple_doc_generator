class Markdown:
    """Represents a markdown file

    Attributes:
        title (str): Title of the markdown document
        content (str): Contains the entire markdown document except
                       the title
        sections (List): MarkdownSection objects.

    Args:
        title (str): Title of the markdown document.
    """

    def __init__(self, title):
        self.name = title
        self.title = "# " + title + "\n"
        self.content = ""
        self.sections = []

    def add_content(self, text):
        """Appends `text` to `content` string."""
        self.content += text

    def add_section(self, section):
        """Appends a MarkdownSection object to `sections`."""
        self.sections.append(section)

    def process_sections(self):
        """Exports all sections into the `content` string."""
        for section in self.sections:
            self.content += section.generate()

    def generate(self, name):
        """Exports `title` and `content` to a markdown file."""
        self.process_sections()
        with open(name, "w") as doc:
            doc.write(self.title)
            doc.write(self.content)


class MarkdownSection:
    """Represents a section in a markdown file
    """

    def __init__(self, title, subsection=False):
        if subsection:
            self.title = "### " + title + "\n"
        else:
            self.title = "## " + title + "\n"
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
        self.content += line + "\n\n"

    def add_list(self, items):
        """Adds a markdown list to the section.

        Args:
            items (List): Strings of the items you want to list.

        Returns:
            Nothing, inplace operation.
        """
        md = ""
        for item in items:
            md += "* " + item + "\n"

        self.content += md + "\n"

    def generate(self):
        return self.title + self.content
