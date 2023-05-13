
n = 5

print(((2 * n)+2 )* "*")
j=0
for i in range(n,0,-1):
    # print(j)
    print("*" * i, " " * j,"*" * i )
    j = j+2

j = j-2
for i in range(1,n+1):
    # print(j)
    print("*" * i, " " * j,"*" * i )
    j = j-2

print(((2 * n)+2 ) * "*"  )