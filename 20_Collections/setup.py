list1 = ["ILIKE","Case-insensitive alternative for LIKE.","ILIKE ANY","Case-insensitive alternative for LIKE ANY."]

answer1 = str(input(f'Question: {list1[1]} \n'))
if str(answer1).upper() ==str(list1[0]).upper():
    print("Correct")
else:
    print("Not Correct")

