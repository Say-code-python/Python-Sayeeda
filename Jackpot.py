
# Program to win Jackpot in 5 rounds of Dice roll

import rolldice # Function to roll three dice at a time

first_name = input("Please enter your name:  ")
print("Welcome " + first_name + " for Jackpot win in 5 Dice rolls. ")

for i in range(1,6):
    input("Please press Enter Key to roll the Dice: " + str(i) + "  attempt")
    result = rolldice.roll()
    print(result)
    if result == (6,6,6): # Jackpot criteria met, 6 in all 3 dice.
        break
    if i == 5: # End of game, completed 5 attempts
        print("Better Luck next time!! Thanks for playing Jackpot")
