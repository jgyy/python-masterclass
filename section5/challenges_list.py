"""
Challenging practice on lists
"""
MENU = []
MENU.append(["egg", "spam", "bacon"])
MENU.append(["egg", "sausage", "bacon"])
MENU.append(["egg", "spam"])
MENU.append(["egg", "bacon", "spam"])
MENU.append(["egg", "bacon", "sausage", "spam"])
MENU.append(["spam", "bacon", "sausage", "spam"])
MENU.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
MENU.append(["spam", "egg", "sausage", "spam"])

# print(MENU)

for meal in MENU:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
