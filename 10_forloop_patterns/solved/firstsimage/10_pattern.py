n = ['A','B','C','D','E']
for j in n:
    for i in n[0:n.index(j)+1]:
        print(i,end=" ")
    print()