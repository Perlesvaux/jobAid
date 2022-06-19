import re
from sys import argv
# read the WYSS section for how to run this
#script, first, second, third = text
#hh1 = content.replace('<p>', '').replace('</p>', '<br>').replace('|', '').replace('\\', '').replace('/', '').replace('"', '').replace(':', '').replace('>', '').replace('<', '')


text = argv[1] # a list of arguments; index 0 will be the .py file itself

with open(text, 'r', encoding="utf8") as f:
    content = f.read()
    hh1 = content.replace('<p>', '').replace('</p>', '<br>')

with open(text, 'w', encoding="utf8") as f:
    f.write(hh1)

with open(text, 'r', encoding="utf8") as f:
    print(f"======================\n{f.read()}\n++++++++++++++++++++++++++++++")


#print(f"este es el texto insertado {text}")