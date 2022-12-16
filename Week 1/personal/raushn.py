# # number guesser 

# import random

# random_number = random.randint(1, 10)

# Player_name = input("Enter your name: ")

# print("The name of the player is " + Player_name )

# guess = int(input("enter your guess number: "))

# attempts = 0


# while attempts == 5:
#     if guess < random_number:
#         print("Your value is too low")
#     elif guess > random_number:
#         print("Your value is too low")
#     elif guess == random_number:
#         print("Hurrah! Your did it")
#     else:
#         break

#     attempts = attempts + 1



# rock, paper, scissors 


import random
user_action = input("Enter a choice(rock, paper, scissors):")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print("Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win")
    else:
        print("paper covers rock! you lose ")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers the rock, You win")
    else:
        print("Scissors cut paper! you lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Paper cut by scissors, You win")
    else:
        print("Scissors placed on rock ! you lose")

