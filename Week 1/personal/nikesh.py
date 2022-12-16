# # number guesser

# import random 

# random_number = random.randint(1,10)
# print(random_number)

# player_name=input("How would you like to call youself: ")
# print(player_name)

# number_of_attempt = 0
# while number_of_attempt < 5:
#         guess = int(input("Enter your guess: "))
#         if guess < random_number:
#             print("Your guess is too low")
#         elif guess > random_number:
#             print("Your guess is too high")
#         elif guess == random_number:
#             print(f"Congratulation! You have successfully guessed the number i.e. {guess}  in {number_of_attempt+1} attempts")
#             break
#         number_of_attempt+=1
#         if number_of_attempt ==5:
#             print(f"Sorry! You couldn't guess the number in 5 tries.Number to be guessed is:{random_number}") 
#         print(f"*"*50)





# rock, paper, scissors 

# import random 
# computer_score = 0
# player_score = 0

# moves = ["rock","scissor","paper"]

# counter = 0

# while counter < 5:
#     random_choice = random.randint(0,10)%3
#     computer =moves[random_choice]
#     # print(f"random number: {random_choice}")

#     player = input("Choose your moves from rock, paper or scissor: ").lower()
#     print("*"*50)
#     print(computer)
#     print(player)
#     print("*"*50)
    
#     if player not in moves:
#         print("Enter valid inputs")
#         continue

#     if computer == player:
#         print("It's a tie")

#     elif computer=="rock":
#         if player == "paper":
#             player_score+=1
#             print("Player wins!!!!!")
#         else:
#             print("Computer wins!!!!")
#             computer_score+=1

#     elif computer=="paper":
#         if player=="rock":
#             print("Computer wins!!!")
#             computer_score+=1
#         else:
#             print("Player wins!!!!")
#             player_score+=1

#     elif computer=="scissor":
#         if player == "paper":
#             print("Computer wins!!!!!")
#             computer_score+=1
#         else:
#             print("Player wins!!!!")
#             player_score+=1

#     counter+=1
#     # print(computer,player)

# print("Total scores:")
# print(f"Computer score: {computer_score}")
# print(f"Player score: {player_score}")

