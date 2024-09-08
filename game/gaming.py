'''
This script contains functions to play the game
'''

# Ignore pylint warnings
# pylint: disable=line-too-long

from configs.constants import Constants
from service.helpers_game import get_computer_move, determine_winner
from utils.logger import logger
from fuzzywuzzy import process


POSSIBLE_MOVES = Constants.Game.POSSIBLE_MOVES
USER_POINTS = Constants.Game.USER_POINTS
COMPUTER_POINTS = Constants.Game.COMPUTER_POINTS


logger.info("Welcome to Rock Paper Scissors!")
NUMBER_ROUNDS = int(input("Enter number of rounds you want to play: "))


logger.info("You will be playing %s against computer", NUMBER_ROUNDS)
for round_cnt in range(NUMBER_ROUNDS):
    user_move = input("Enter your move (rock, paper, or scissors): ").lower()
    user_move, fuzzy_match = process.extractOne(user_move, POSSIBLE_MOVES)
    user_move = user_move if fuzzy_match >= 60 else (_ for _ in ()).throw(Exception("Invalid move"))
    computer_move = get_computer_move()
    
    




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
