import sys
for i in sys.path:
    print(i)
import b # File a.py

b.spam('gumby')

# print(d)
# print(a)


print(b.d)
# print(b.a)

print(b.c.a)
"""Load the file b.py (unless it’s already loaded), and give me access to all its attributes
through the name b.
"""

x = 200
