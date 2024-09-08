'''
Configurations for logging
'''

# Ignore pylint warnings
# pylint : disable = line-too-long


import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s %(asctime)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename='game.log',
    filemode='w'
    )

logger = logging.getLogger()