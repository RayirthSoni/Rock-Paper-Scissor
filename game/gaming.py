'''
This script contains functions to play the game
'''

# Ignore pylint warnings
# pylint: disable=line-too-long

import random
from fuzzywuzzy import process


USER_POINTS = 0
COMPUTER_POINTS = 0


POSSIBLE_MOVES = ['rock', 'paper', 'scissors']
num_rounds = int(input('Enter number of rounds you want to play: '))

def get_computer_move() -> str:
    """Function is used to get random move chosen by computer

    Returns:
        str: Random move chosen by computer
    """
    return random.choice(POSSIBLE_MOVES)

computer_move = get_computer_move()

def determine_winner():
    pass


for i in range(num_rounds):
    user_move = input('Enter your move (rock, paper, or scissors): ').lower()
    user_move, fuzzy_match = process.extractOne(user_move, possible_moves)
    computer_move = random.choice(possible_moves)
    


def start_game():
        

        print(f'Round {i + 1}: You chose {user_move}, Computer chose {computer_move}')

        if (
            (user_move == 'rock' and computer_move == 'scissors') or
            (user_move == 'paper' and computer_move == 'rock') or
            (user_move == 'scissors' and computer_move == 'paper')
        ):
            user_points += 1
            print('You win this round!')
        elif (
            (computer_move == 'rock' and user_move == 'scissors') or
            (computer_move == 'paper' and user_move == 'rock') or
            (computer_move == 'scissors' and user_move == 'paper')
        ):
            computer_points += 1
            print('Computer wins this round!')
        else:
            print("It's a draw!")

    print(f'All {num_rounds} rounds finished !')
    print(f'Your Points = {user_points}')
    print(f'Computer Points = {computer_points}')

    if user_points > computer_points:
        print('You win the game!!')
    elif user_points < computer_points:
        print('Computer wins the game!!')
    else:
        print("It's a draw!")

if __name__ == "__main__":
    start_game()
