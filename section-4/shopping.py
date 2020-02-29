"""
An assign on shipping list
"""
SHOPPING_LIST = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in SHOPPING_LIST:
    if item == "spam":
        break

    print("Buy " + item)
