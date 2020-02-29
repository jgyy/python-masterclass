"""
Find the highest and lowest
"""
LOW = 0
HIGH = 99999999

print("Please think of a number between {} and {}".format(LOW, HIGH))
input("Press ENTER to start")

GUESSES = 1
while LOW != HIGH:
    print("\tGuessing in the range of {} to {}".format(LOW, HIGH))
    guess = LOW + (HIGH - LOW) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        LOW = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess
        HIGH = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(GUESSES))
        break
    else:
        print("Please enter h, l or c")

    GUESSES += 1
else:
    print("You thought of the number {}".format(LOW))
    print("I got it in {} guesses".format(GUESSES))
