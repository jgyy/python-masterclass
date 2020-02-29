"""
To search for item within shopping list
"""
SHOPPING_LIST = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

ITEM_TO_FIND = "albratross"
FOUND_AT = None

for index in range(len(SHOPPING_LIST)):
    if SHOPPING_LIST[index] == ITEM_TO_FIND:
        FOUND_AT = index
        break

if ITEM_TO_FIND in SHOPPING_LIST:
    FOUND_AT = SHOPPING_LIST.index(ITEM_TO_FIND)

if FOUND_AT is not None:
    print("Item found at position {}".format(FOUND_AT))
else:
    print("{} not found".format(ITEM_TO_FIND))
