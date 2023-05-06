# import sys
# sys.argv[]


# print(a)
# fun1()

# def fun1():
#     pass


# line breaking
# print("Coforge is people. To show our appreciation we’re gifting all our \
#       23,000+ employees an iPad. Thank you for being an integral part \
#           of our journey and helping us reach this milestone.")


# print("""Coforge is people. To show our appreciation we’re gifting all our 
#       23,000+ employees an iPad. Thank you for being an integral part 
#           of our journey and helping us reach this milestone.""")


# # automation line breaking.
# import pandas as pd

# import pandas as pd

# data = pd.read_csv(r'C:\Users\Ron\Desktop\products_sold.csv')   
# df = pd.DataFrame(data,
#                   columns=['product',
#                            'price'])
# print(df)

# a = input("enter your username :")
# a = "safd"
# b = "wersd"
# print("Hello",a,b,"bye")

# print("Hello "+a+" "+b+" bye")

# print(f'Hello {a} {b} bye')
# print(f'Hello {a} {b} bye')

# x=10
# def fun1():
#     x=20
#     print("outer",x)
#     def fun2():
#         global x
#         print()
#         print("inner",x)
        
#     fun2()

# fun1()


from math import * 

global var 
var = 3000
def outer_func_1():
    # var = 5000
    def outer_func():
        # This block is the Local scope of outer_func()
        # var = 100  # A nonlocal var
        # It's also the enclosing scope of inner_func()
        # for i in range(1):
        #     var = 200
            
        def inner_func():
            # global var
            # var = 10
            x = var + 100
            # This block is the Local scope of inner_func()
            print(f"Printing var from inner_func(): {var}")
            # var = var+1000

        inner_func()
        print(var)
        print(f"Printing var from outer_func(): {var}")

    outer_func()
print(pi)
outer_func_1()
# print(f"Printing var from outside(): {var}")

    # Local
    # Enclosing
    # Global
    # Builtin