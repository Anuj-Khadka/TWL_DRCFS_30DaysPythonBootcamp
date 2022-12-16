# import random 

# random_number = random.randint(1, 10)
# i = 1
# while(i <= 5):
#     guess = int(input("guess a number between 1 to 10: "))
#     if guess == random_number:
#         print("You are correct")
#         print(f"you guessed the number in {i} tries")
#         break
#     elif guess > random_number:
#         print("your guess is too high")
        
#     elif guess > random_number:
#         print("your guess is too low")
        
#     i+=1







from random import random, randint, choices
moves=['rock','paper','scissors']

while True:
    computer = moves[randint(0,2)]
    # computer_move = random.choices(moves)
    player = input('rock, paper or scissors?(or end the game)').lower()
    if player =='end the game':
        print("The game has ended")
        break

    elif player == computer:
        print('tie') 

    elif player == 'rock':
        if computer == 'paper':
            print('you lose', computer,'beats',player)
        else:
            print('you  win', player, 'beats',computer)
            

    elif player == 'paper':
        if computer == 'scissors':
            print('you lose', computer,'beats',player)
        else:
            print('you  win', player, 'beats',computer)  
            

    elif player == 'scissors':
        if computer == 'paper':
            print('you lose', computer,'beats',player)
        else:
            print('you  win', player, 'beats',computer)  
            
    
    else:
         print('check your spelling...')

         

