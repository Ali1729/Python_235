from datetime import datetime
l = range(100000)

def square_g(l):
    for i in l:        
        
        yield i**2
        
start_time = datetime.now()
l2 = square_g(l)

print(type(l2))
print(len(list(l2)))
print(datetime.now() - start_time)
for i in l2:
    if i<100:
        print(i)