lea# 9
# 9. Write a program that asks the user to input n , create a list of n values
#  and then prints out only the even numbers. Use the continue statement to skip over odd numbers.

a = list(range(int(input("Enter one number"))))

for i in a:
    if i%2 !=0:
        continue
    else:
        print(i)