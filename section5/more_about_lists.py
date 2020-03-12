"""
This script expands more about lists.
"""
# LIST_1 = []
# LIST_2 = list()

# print("List 1: {}".format(LIST_1))
# print("List 2: {}".format(LIST_2))

# if LIST_1 == LIST_2:
#     print("The lists are equal")

# print(list("The lists are equal"))
# EVEN = [2, 4, 6, 8]

# ANOTHER_EVEN = sorted(even, reverse=True)

# print(ANOTHER_EVEN is EVEN)

# ANOTHER_EVEN.sort(reverse=True)
# print(EVEN)
EVEN = [2, 4, 6, 8]
ODD = [1, 3, 5, 7, 9]

NUMBERS = [EVEN, ODD]

for number_set in NUMBERS:
    print(number_set)

    for value in number_set:
        print(value)
