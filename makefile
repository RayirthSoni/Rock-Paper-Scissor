# Makefile

# Set the root directory for PYTHONPATH
ROOT_DIR := $(shell pwd)

# Default environment variable to use the root directory as PYTHONPATH
export PYTHONPATH := $(ROOT_DIR)

# Task to run the game script
run:
	python3 server.py
