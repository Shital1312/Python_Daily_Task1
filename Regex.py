import re

#
# prog = re.compile(r'm\w\w')
# line = 'sat cat mat pat rat'
# result = prog.search(line)
# print(result.group())

#search
# sentence = 'manllll can sun mop run'
# result = re.search(r'm\w\w', sentence)
# print(result.group())

#finall
# sentence = 'manllll can sun mop run'
# result = re.findall(r'm\w\w', sentence)
# print(result)

#match()
sentence = 'mao can sun mop run'
result = re.match(r'm\w\w', sentence)
print(result)


text = "Please contact me at john@example.com or jane@example.com"
pattern = r'\w+@\w+\.\w+'

matches = re.findall(pattern, text)
for match in matches:
    print(match)
