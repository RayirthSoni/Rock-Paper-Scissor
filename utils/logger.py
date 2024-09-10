"""
Configurations for logging
"""

# Ignore pylint warnings
# pylint : disable = line-too-long


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)
