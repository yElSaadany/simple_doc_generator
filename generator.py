from docstring_parser import parse

def extract_docstring(file):
    with open(file, 'r') as doc:
        lines =  doc.readlines()
    
    tmp = []
    new_docstring = False
    in_class = False
    for line in lines:
        if("class" in line and not(in_class)):
            current = "class " + line[6:-2]
            in_class = True
        elif('"""' in line and not(new_docstring)):
            tmp.append(line)
            new_docstring = True
        elif('"""' in line and new_docstring):
            tmp.append(line)
            new_docstring = False
            in_class = False
            tmp = ''.join(tmp)
            return {current: tmp}
        elif(new_docstring):
            tmp.append(line)
        else:
            pass
        

def generate_markdown(docstring):
    for key, value in docstring.items():
        md = []

        md.append("# %s" % key)
        docstring = parse(value)
        print(docstring.params[0].arg_name)
        md.append("## Arguments")
        for i in range(len(docstring.params)):
            tmp = "* %s (*%s*): %s" %(docstring.params[i].arg_name,
             docstring.params[i].type_name,
             docstring.params[i].description)
            
            md.append(tmp)
        return md