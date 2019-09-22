import generator

res = generator.extract_docstring('cleaner.py')
md = generator.generate_markdown(res)

[print(line) for line in md]
