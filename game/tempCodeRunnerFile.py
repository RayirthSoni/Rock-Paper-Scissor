from configs.constants import Constants
from service.helpers_game import get_computer_move, determine_winner
from fuzzywuzzy import process


POSSIBLE_MOVES = Constants.Game.POSSIBLE_MOVES
USER_POINTS = Constants.Game.USER_POINTS
COMPUTER_POINTS = Constants.Game.COMPUTER_POINTS


NUMBER_ROUNDS = int(input("Enter number of rounds you want to play: "))

for round_cnt in range(NUMBER_ROUNDS):
    user_move = input("Enter your move (rock, paper, or scissors): ").lower()
    user_move, fuzzy_match = process.extractOne(user_move, POSSIBLE_MOVES)
    user_move = user_move if fuzzy_match >= 60 else (_ for _ in ()).throw(Exception("Invalid move"))
    computer_move = get_computer_move()