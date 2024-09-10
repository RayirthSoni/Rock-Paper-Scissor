"""
Script contains flow to play the game
"""

# Ignore pylint warnings
# pylint: disable=line-too-long


from configs.constants import Constants
from game.gaming import play_game
from utils.logger import logger


USER_POINTS = Constants.Game.USER_POINTS
COMPUTER_POINTS = Constants.Game.COMPUTER_POINTS


def gaming():
    """
    Function is used for flow of the game
    """
    logger.info("Welcome to Rock Paper Scissors!")
    NUMBER_ROUNDS = int(input("Enter number of rounds you want to play: "))
    logger.info("You will be playing %s rounds against computer", NUMBER_ROUNDS)
    play_game(NUMBER_ROUNDS, USER_POINTS, COMPUTER_POINTS)


if __name__ == "__main__":
    gaming()
