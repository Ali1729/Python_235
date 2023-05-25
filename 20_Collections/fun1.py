from datetime import datetime
l = range(100000)

def square(l):
    l2 = []
    for i in l:
        
        l2.append(i**2)
        
    return l2

start_time = datetime.now()
l2 = square(l)
print(len(list(l2)))
print(datetime.now() - start_time)
print(type(l2))
for i in l2:
    if i<100:
        print(i)