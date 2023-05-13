# Python program to read
# json file


import json
import os

# Opening JSON file
f = open( os.path.realpath('.')+'data.json')
# 'c:\\Users\\LENOVO\\Desktop\\Python_235data.json'
# C:\Users\LENOVO\Desktop\Python_235\08_09_files\data.json
# : 'C:\\Users\\LENOVO\\Desktop\\Python_235\\08_09_files\\loading_json.pydata.json'

a = '{ "id": "1001", "type": "Regular" }'
# returns JSON object as
# a dictionary

data = json.load(f)
# print(data)
# print(type(data))
# Iterating through the json
# list
for i in data['topping']:
	print(i)

# Closing file
f.close()
