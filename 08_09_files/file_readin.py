# fp = open('a1.txt','r') 

# file_content = fp.readlines()

# print(type(file_content))
# print("\n\n\n")

# for i in file_content:
#     print(i)


# fp.close()


with open('a1.txt','r') as fp:
    file_content = fp.readlines()
    print(" number of times")
    

for i in file_content:
    print(i)