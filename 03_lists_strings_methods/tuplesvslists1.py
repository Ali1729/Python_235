import time

my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]

start_time = time.time()
for i in range(100000000):
    for item in my_tuple:
        pass
print("Time taken for tuple iteration:", time.time() - start_time)

start_time = time.time()
for i in range(100000000):
    for item in my_list:
        pass
print("Time taken for list iteration:", time.time() - start_time)
