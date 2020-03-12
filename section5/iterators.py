"""
Understanding iterators in this script
"""
STRING = "1234567890"

# for char in STRING:
#     print(char)
# MY_ITERATOR = iter(STRING)
# print(MY_ITERATOR)
# print(next(MY_ITERATOR))

for char in STRING:
    print(char)

for char in iter(STRING):
    print(char)
