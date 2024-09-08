"""
Constants
"""

# Ignore pylint warnings
# pylint: disable=line-too-long


class Constants:
    """
    Constants configurations
    """

    class Game:
        """
        Game constants
        """

        POSSIBLE_MOVES = ["rock", "paper", "scissors"]
        USER_POINTS = 0
        COMPUTER_POINTS = 0
        OUTCOMES = {
            ("rock", "scissors"): "win",
            ("scissors", "paper"): "win",
            ("paper", "rock"): "win",
        }
