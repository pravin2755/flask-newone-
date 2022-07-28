import logging
import sys

logger = logging.getLogger()  # use for log generate

loggers = {}
FORMATTER = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("test.log", "a", "utf8")
file_handler.setFormatter(FORMATTER)
logger.addHandler(file_handler)
logger.propagate = False
loggers["test"] = logger

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
