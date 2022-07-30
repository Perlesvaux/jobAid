import re
from sys import argv
# read the WYSS section for how to run this
#script, first, second, third = text
#hh1 = content.replace('<p>', '').replace('</p>', '<br>').replace('|', '').replace('\\', '').replace('/', '').replace('"', '').replace(':', '').replace('>', '').replace('<', '')


text = argv[1] # a list of arguments; index 0 will be the .py file itself

# with open(text, 'r', encoding="utf8") as f:
#     content = f.read()
#     hh1 = content.replace('IATA \u2013 ', '')


# with open(text, 'w', encoding="utf8") as f:
#     f.write(hh1)

# with open(text, 'r', encoding="utf8") as f:
#     print(f"======================\n{f.read()}\n++++++++++++++++++++++++++++++")









# rep = argv[2]

# with open(text, 'r', encoding="utf8") as f:
#     comp = []
#     for eachline in f:
#         part1 = eachline[:3]
#         part2 = f'{eachline[4:len(eachline)-1]}'
#         replacement = ':' #eachline[5]
#         comp.append(f'"{part1}"{replacement}"{part2}",')

#     with open(rep, 'w', encoding="utf8") as r:
#         for entry in comp:
#             r.write(entry)




with open(text, 'r', encoding="utf8") as f:
    for eachline in f:
        print(eachline.lower())









# for x in comp:
    
#     print(x.replace(x[5], '":"'))

#######
# string = "some, thing"
# string1 = string[:4]
# string2 = string[5: len(string)]
# replacement = "B==D ---<3"
# whole = f"{string1} {replacement} {string2}"
# print(whole)






#print(f"este es el texto insertado {text}")  -----\u2013------^([^,]+),


