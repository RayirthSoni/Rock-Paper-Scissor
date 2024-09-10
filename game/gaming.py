"""
This script contains function for playing the game
"""

# Ignore pylint warnings
# pylint: disable=line-too-long

from configs.constants import Constants
from service.helpers_gaming import get_computer_move, determine_winner
from utils.logger import logger
from fuzzywuzzy import process


POSSIBLE_MOVES = Constants.Game.POSSIBLE_MOVES


def play_game(
    number_rounds: int, final_user_points: int, final_computer_points: int
) -> None:
    """
    Function is used to play the game
    """
    for round_cnt in range(number_rounds):
        user_move = input("Enter your move (rock, paper, or scissors): ").lower()
        user_move, fuzzy_match = process.extractOne(user_move, POSSIBLE_MOVES)
        user_move = (
            user_move
            if fuzzy_match >= 60
            else (_ for _ in ()).throw(Exception("Invalid move"))
        )

        computer_move = get_computer_move()
        user_points, computer_points = determine_winner(user_move, computer_move)

        final_user_points += user_points
        final_computer_points += computer_points

        logger.info(
            "Round %s - User chose %s, Computer chose - %s - User Points %s, Computer Points %s",
            round_cnt + 1,
            user_move,
            computer_move,
            final_user_points,
            final_computer_points,
        )
