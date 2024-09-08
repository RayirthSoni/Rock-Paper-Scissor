"""
Scirpt containing functions used to play game
"""

# Ignore pylint warnings
# pylint: disable=line-too-long

import random
from typing import Tuple
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


def determine_winner(user_move: str, computer_move: str) -> Tuple[int, int]:
    """Function is used to determine who won the round based on user move and computer move

    Args:
        user_move (str): Move chosen by user
        computer_move (str): Move chosen by computer

    Returns:
        Tuple[int, int]: user points, computer points
    """

    user_status = OUTCOMES.get((user_move, computer_move), None)
    computer_status = OUTCOMES.get((computer_move, user_move), None)

    if user_status:
        return 1, 0
    elif computer_status:
        return 0, 1
    else:
        return 0, 0
