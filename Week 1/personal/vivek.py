# Scissors, paper, rock 

# import random

# print("1. rock, 2. paper, 3. scissors")

# i=0
# while i<=4:
#     selection = int(input('Enter user throw: '))

#     if (selection == 1):
#         user_throw= "Rock"
#     elif selection == 2:
#         user_throw="Paper"
#     elif selection == 3: 
#         user_throw = "Scissors"

#     print('Player Throws', user_throw)

#     throws= ["Rock", "Paper","Scissors"]
#     comp_throw = random.choice(throws)

#     print('Computer throws', comp_throw)

#     if user_throw == comp_throw:
#         print("Tie Game")

#     elif user_throw == "Rock":
#         if comp_throw == "Paper":
#             print("Comp Wins")
#         elif comp_throw == "Scissors":
#             print("Player Wins")

#     elif user_throw == "Paper":
#         if comp_throw == "Scissors":
#             print("Comp Wins")
#         elif (comp_throw == "Rock"):
#             print("Player Wins")

#     elif user_throw == "Scissors":
#         if comp_throw == "Rock":
#             print("Comp Wins")
#         elif (comp_throw == "Paper"):
#             print("Player Wins")
    
#     i = i + 1
    
  
################################################################################################

#   Number guesser

import random
random_number = random.randint(1, 10)

player_name = input('Enter a name: ')
print(player_name)

# as the "i" term has a purpose, try using some meaningful variable like "chance" or so
i = 1
while i <= 5:
    guess = int(input('Enter a number between 1 to 10 -> '))
    if guess == random_number:
        print(f'{player_name} guessed the number. \nYour guess is right in {i} times')
        break

    elif guess > random_number:
        print('guess a smaller number')

    elif guess < random_number:
        print("guess a bigger number")

    print(f'{5-i} chances remains')

    i = i+1

