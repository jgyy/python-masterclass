"""
This script writes a simple adventure journey
"""
AVAILABLE_EXITS = ["north", "south", "east", "west"]

CHOSEN_EXIT = ""
while CHOSEN_EXIT not in AVAILABLE_EXITS:
    CHOSEN_EXIT = input("Please choose a direction: ")
    if CHOSEN_EXIT == "quit":
        print("Game over")
        break
else:
    print("aren't you glad you got out of there")
