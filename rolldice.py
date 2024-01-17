# Function to roll 3 dice and check jackpot criteria of 6 in all 3 dice.
# And return the dice result for each roll

import random
def roll():
    first_number = random.randint(1, 6)
    second_number = random.randint(1, 6)
    third_number = random.randint(1, 6)
    if (first_number == 6 and second_number == 6 and third_number == 6):
        print("Jackpot, Won $1000")
        print("Congratulation!! Thanks for playing Jackpot")
    else:
        print("Missed, Roll again ")
    return first_number, second_number, third_number