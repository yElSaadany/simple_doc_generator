from docstring_parser import parse

def extract_docstring(file):
    with open(file, 'r') as doc:
        lines =  doc.readlines()
    
    tmp = []
    ret = {}
    new_docstring = False
    in_docstring = False
    in_class = False
    for line in lines:
        if("class" in line and not(in_docstring)):
            # The beginning of a class
            current = "class " + line[6:-2]
            new_docstring = True
        elif("def" in line and not(in_docstring)):
            # The beginning a of method/function
            if(line[:4] == '    '): # Means it's a method, not a function
                current = "method " + line[8:-2]
            else:
                current = "function " + line[4:-2] # It's a function
        elif('"""' in line and not(in_docstring)):
            # It's the start of the docstring
            tmp.append(line)
            in_docstring = True
        elif('"""' in line and in_docstring):
            # It's the end of the docstring
            tmp.append(line)
            in_docstring = False
            new_docstring = False
            tmp = ''.join(tmp)
            ret.update({current: tmp})
            tmp = []
        elif(in_docstring):
            tmp.append(line)
        else:
            pass
    
    return ret
        

def generate_markdown(docstring):
    class_name = None
    md = []
    for key, value in docstring.items():
        docstring = parse(value)
        # if function class name None
        # Meta
        ## If a class name is defined, then the key is a method
        if class_name:
            md.append("## %s" % key)
        else:
            md.append("# **%s**" % key)
        md.append(docstring.short_description[3:] + "\n")
        md.append(docstring.long_description)
        md.append("### Arguments")
        for i in range(len(docstring.params)):
            tmp = "* %s (*%s*): %s" %(docstring.params[i].arg_name,
             docstring.params[i].type_name,
             docstring.params[i].description)
            
            md.append(tmp)
        if docstring.returns:
            md.append("### Returns")
            md.append(docstring.returns.description[:-5])
        
        if "class" in key:
            class_name = key[6:-2]

    return md