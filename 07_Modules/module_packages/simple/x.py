import y # File a.py

# from y import *

from y import d

# def spam(text): # File b.py
#     print(text, 'spam')
    
# spam('gumby')   
# b.spam('gumby')

d = 300

print(d)
# print(a)
# y.g

print(y.d)
# print(b.a)

print(y.z.a)
# print(z.a)
"""Load the file b.py (unless it’s already loaded), and give me access to all its attributes
through the name b.
"""

