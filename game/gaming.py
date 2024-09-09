"""
This script contains functions to play the game
"""

# Ignore pylint warnings
# pylint: disable=line-too-long

from configs.constants import Constants
from service.helpers_gaming import get_computer_move, determine_winner
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
    user_move = (
        user_move
        if fuzzy_match >= 60
        else (_ for _ in ()).throw(Exception("Invalid move"))
    )

    computer_move = get_computer_move()
    user_points, computer_points = determine_winner(user_move, computer_move)

    logger.info(
        "Round %s - User chose %s, Computer chose - %s - User Points %s, Computer Points %s",
        round_cnt + 1,
        user_move,
        computer_move,
        USER_POINTS,
        COMPUTER_POINTS,
    )

    USER_POINTS += user_points
    COMPUTER_POINTS += computer_points
