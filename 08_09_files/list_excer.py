# square each member of the list
a = [1,2,3,4,5]
# j = []
# for i in a:
#     if i%2 ==0:
#         j.append(i*i)
    
# # print(j)

# new_list = [expression for item in old_list if condition]
# new_list = [expression for item in [expression for item in old_list2] if condition]

j = [i*i for i in a if i%2 == 0]
# ()
# {}
print(j)