"""This module is used to configure our loggers
   We particularly focus on logging debug and error logs
"""
import logging
import os

# Create a logger for debug messages
debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)

# Create a logger for error messages
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)

# Create handlers for debug and error log files
debug_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__),'logs/debug.log'))
error_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__),'logs/errors.log'))

# Create a formatter for the log messages
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Add the handlers to their respective loggers
debug_logger.addHandler(debug_handler)
error_logger.addHandler(error_handler)
