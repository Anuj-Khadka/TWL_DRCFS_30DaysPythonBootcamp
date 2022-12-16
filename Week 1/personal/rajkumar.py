# # number guesser 

# import random
# random_number = random.randint(1,10)
# for _ in range(5):
#     guess = int (input("Enter your guess number between 1 to 20"))
#     if guess==random_number:
#         print("your guess is right")
#         break
#     elif guess>random_number:
#         print("your guess is greater than random number")
    
#     elif guess<random_number:
#         print("your guess is lower than random number")




# rock, paper, scissors 

import random

user_action=input("Enter a choice(rock, paper, scissors):")
possible_actions= ["rock","paper","scissors"]

computer_action = random.choice(possible_actions)

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")