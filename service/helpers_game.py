"""
Scirpt containing functions used to play game
"""

# Ignore pylint warnings
# pylint: disable=line-too-long

import random
from fuzzywuzzy import process
from configs.constants import Constants


POSSIBLE_MOVES = Constants.Game.POSSIBLE_MOVES
OUTCOMES = Constants.Game.OUTCOMES


def get_computer_move() -> str:
    """Function is used to get random move chosen by computer
    Returns:
        str: random move chosen by computer
    """
    return random.choice(POSSIBLE_MOVES)


def determine_winner(user_move: str, computer_move: str):
    
    outcome = OUTCOMES[(user_move, computer_move)]
    
    
    pass
