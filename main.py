import random
import click
print('')
print('Welcome to Rock Paper Scissors game')
print('')
print('You\'ll be playing against the CPU')
while True:

    playable_list = ['R', 'P', 'S']

    print('')

    print('Enter R for Rock, P for Paper or S for Scissors')
    

    while True:
        player_one = input('Enter your choice [R, P or S] here: ')
        player_one = player_one.lower()
        playable_list = [x.lower() for x in playable_list]
        if player_one not in playable_list:
            print('Your move is invalid')
            continue
        else:
            break


    player_two = random.choice(playable_list)
    print(' ')

    if player_one == 'r':
        player_one = 'Rock'
    elif player_one == 'p':
        player_one = 'Paper'
    elif player_one == 's':
        player_one = 'Scissors'


    if player_two == 'r':
        player_two = 'Rock'
    elif player_two == 'p':
        player_two = 'Paper'
    elif player_two == 's':
        player_two = 'Scissors'


    print('You (Player) played', player_one)
    print('Computer (CPU) played', player_two)

    print(' ')

    if player_one == player_two:
        print('It\'s a tie!')
        print('We\'ll go into tiebreaker round now')
        continue
    elif player_one == 'Rock' and player_two == 'Scissors':
        print('Rock breaks Scissors')
        print('You won!')
    elif player_one == 'Rock' and player_two == 'Paper':
        print('Paper covers Rock')
        print('Computer won!')
    elif player_one == 'Scissors' and player_two == 'Rock':
        print('Rock breaks Scissors')
        print('Computer won!')
    elif player_one == 'Scissors' and player_two == 'Paper':
        print('Scissors cuts Paper')
        print('You won!')
    elif player_one == 'Paper' and player_two == 'Scissors':
        print('Scissors cuts Paper')
        print('Computer won!')
    elif player_one == 'Paper' and player_two == 'Rock':
        print('Paper covers Rock')
        print('You won!')

    print('')
    print('Good Bye and see you again!')
    print('')
    break
   
