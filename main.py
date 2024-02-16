import random


# all possible moves
possible_moves = ['rock', 'paper', 'scissor']

# number of round you wish to play
num_rounds = int(input('Enter number of rounds you want to play : '))
print()

# points which both user and computer have initially
user_points = computer_points = 0

for i in range(num_rounds):

    # move made by user and computer
    user_move = input('Enter your move : ')
    computer_move = random.choice(possible_moves)

    # converting user move to lowercase
    user_move = user_move.lower()

    if user_move == 'rock':
        if computer_move == 'paper':
            computer_points += 1
        elif computer_move == 'scissor':
            user_points += 1
            
    elif user_move == 'paper':
        if computer_move == 'rock':
            user_points += 1
        elif computer_move == 'scissor':
            computer_points += 1
            
    elif user_move == 'scissor':
        if computer_move == 'rock':
            computer_points += 1
        elif computer_move == 'paper':
            user_points += 1

print(f'\nAll {num_rounds} rounds finished !')

print(f'\nUser Points = {user_points}\nComputer Points = {computer_points}\n')

if user_points > computer_points:
    print('User Wins !!')
elif user_points < computer_points:
    print('Computer Wins !!')
else:
    print('Draw')