# 10. Write a program that asks the user to input a series of words,
#  and then prints out only the words that start with a vowel. Use the continue statement to skip over words that don't start with a vowel.


input_value = input("Enter string values ").strip()
# input_values = input_value.strip(" ")
input_values = input_value.split(" ")
print(input_values)
for i in input_values:
    if (not(i[0] == 'A' or i[0] == 'a'
        or i[0] == 'E' or i[0] == 'e'
        or i[0] == 'I' or i[0] == 'i'
        or i[0] == 'O' or i[0] == 'o'
        or i[0] == 'U' or i[0] == 'u')) :
        continue
    else:
        print(i)