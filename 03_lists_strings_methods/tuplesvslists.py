import time
a_list = list(range(10000000))
a_tuple = tuple(range(10000000))

start_time = time.time()
for i in a_tuple:
    pass

print()
print(time.time() - start_time)

start_time = time.time()
for i in a_list:
    pass

print(time.time() - start_time)
