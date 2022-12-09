# # rock paper scissors

# import random

# possible_actions = ["rock", "paper", "scissors"]


# # computer_action = random.choice(possible_actions)

# plays = 1

# while plays <= 5:
#     computer_action = random.choice(possible_actions).lower()
#     user_action = input("Enter a choice(rock, paper, scissors): ").lower()

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")

#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("You win")
#         else:
#             print("paper covers rock! you lose ")

#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers the rock, You win")
#         else:
#             print("Scissors cut paper! you lose")

#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Paper cut by scissors, You win")
#         else:
#             print("Scissors placed on rock ! you lose")


#     if user_action not in possible_actions:
#         print("enter a valid action")

#     plays += 1


#################################################################################################

##number guesser

import random
random_number = random.randint(1, 10)
Player_name = input("Enter your name: ")
print("The name of the player is " + Player_name )

attempts = 1

while attempts <= 5:
    guess = int(input("enter your guess number: "))
    if guess == random_number:
        print("Hurrah! Your did it")
        break
    elif guess < random_number:
        print("Your value is too low")
    elif guess > random_number:
        print("Your value is too high")
    

    attempts += 1

    if attempts > 5:
        print("Sad! you didn't make it well")