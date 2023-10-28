"""This module is used to log errors and debug messages to a file.
"""
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
"""Create a logger to log debug messages and errors.
"""

debug_handler = logging.FileHandler(
    './logs/debug.log')
error_handler = logging.FileHandler(
    './logs/errors.log')
"""Create a handler to log debug messages to a file.
"""

debug_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.ERROR)

logger.addHandler(debug_handler)
logger.addHandler(error_handler)


formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
"""Create a formatted message for the logs.
"""
debug_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
