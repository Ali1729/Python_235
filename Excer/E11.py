import copy

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
copy_list = copy.deepcopy(nested_list)

for sublist in nested_list:
    for i in range(len(sublist)):
        sublist[i] *= 2

print("Original list:", nested_list)
print("Copied list:", copy_list)