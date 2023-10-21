import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

debug_handler = logging.FileHandler('logs/debug.log')
error_handler = logging.FileHandler('logs/errors.log')

debug_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.ERROR)

logger.addHandler(debug_handler)
logger.addHandler(error_handler)

formatter = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
debug_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
