# Python program to read
# json file


import json

# Opening JSON file
f = open(r'C:\Users\LENOVO\Desktop\Python_235\08_files\data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['topping']:
	print(i)

# Closing file
f.close()
