
# random purain impost garda hunxa
# import random
import random

moves=['rock','paper','scissors']


# randint(1,10)
player_win = 0
computer_win = 0


plays = 1
while plays <= 5:

# while True:
    # random.choice() --- used in list/tuples, choose from a list
    # computer =moves[randint(0,2)]
    computer_move = random.choice(moves)
    player = input('rock,paper or scissors?(or end the game)').lower()

    if player == computer_move:
        print('tie') 
        # computer_win += 1
        print(f'Your score: {player_win}\t Computer score: {computer_win}')

    elif player == 'rock':
        if computer_move == 'paper':
            print('you lose', computer_move,'beats',player)
            computer_win += 1
            print(f'Your score: {player_win}\t Computer score: {computer_win}')
        else:
            print(f'you  win {player} beats {computer_move}')

    elif player == 'paper':
        if computer_move == 'scissors':
            print('you lose', computer_move,'beats',player)
        else:
            print('you  win', player, 'beats',computer_move)  
            

    elif player == 'scissors':
        if computer_move == 'paper':
            print('you lose', computer_move,'beats',player)
        else:
            print('you  win', player, 'beats',computer_move)  
            
    
    if player not in moves:
         print('check your spelling...')


    # plays += 1

         
