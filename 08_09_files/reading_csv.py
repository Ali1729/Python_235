with open("a1.csv",'r') as fp:
    content = fp.readlines()
    
# print(content)

header = content[0]
rows = []
for i in content[1:]:
    rows.append(i.split(','))

header = header.split(',')
print(header)
print(rows)

print(rows[1][2])