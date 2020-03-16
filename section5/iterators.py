"""
Understanding iterators in this script
"""
STRING = "1234567890"

for char in STRING:
    print(char)
MY_ITERATOR = iter(STRING)
print(MY_ITERATOR)
print(next(MY_ITERATOR))

for char in STRING:
    print(char)

for char in iter(STRING):
    print(char)

MY_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

MY_ITERATOR = iter(MY_LIST)

for index in range(0, len(MY_LIST)):
    next_item = next(MY_ITERATOR)
    print(next_item)

for index in MY_LIST:
    print(index)
