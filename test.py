import generator

res = generator.extract_docstring('<python_file.py>')
md = generator.generate_markdown(res)

with open('test.md', 'w') as doc:
    for line in md:
        doc.write(line)
        doc.write("\n")
