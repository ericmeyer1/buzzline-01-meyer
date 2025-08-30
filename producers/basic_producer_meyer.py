"""
basic_generator_meyer.py

Custome producer generating simple manufactured log messages.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be logged every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating manufacturing messages
MACHINES: list = ["Press-101", "CNC-204", "Lathe-330", "Welder-112", "Robot-7"]
ACTIONS: list = ["started job", "completed job", "stopped for maintenance", "resumed operation", "waiting for material"]
STATUS: list = ["OK", "Warning", "Error"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    """
    Generate a stream of manufacturing log messages.
    """
    while True:
        machine = random.choice(MACHINES)
        action = random.choice(ACTIONS)
        status = random.choice(STATUS)
        yield f"[{machine}] {action} | Status: {status}"


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for manufacturing log producer.
    """
    logger.info("START Manufacturing Log Producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")

    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()
