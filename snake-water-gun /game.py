
import random
"""
Snake, Water, Gun Game
Snake = 1
Water = -1
Gun = 0
"""

computer = random.choice([1, -1, 0])
youStr = input("Enter your choice: Snake, Water, Gun: ")
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
revDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"Computer chose: {revDict[computer]} \n You chose: {youStr}") # revDict[computer] is used to get the value of the key in the dictionary

if(computer == you):
    print("It's a draw")

else:
    if(computer == 1 and you == -1):
        print("Computer wins")
    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("Computer wins")

    elif(computer == 0 and you == 1):
        print("Computer wins")
    elif(computer == 0 and you == -1):
        print("You win")

    else:
        print("Invalid input")

