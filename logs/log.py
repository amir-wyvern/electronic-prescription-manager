import logging

"""
This module is only for displaying the color logs of the program 
so that the logs can be checked better
"""

class CustomFormatter(logging.Formatter):

    cyan = "\x1b[36m"
    grey = "\x1b[37m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    # red = "\x1B[31m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(name)-3s -%(process)-7d-%(levelname)-8s] [%(asctime)-24s] | %(message)s"

    FORMATS = {
        logging.DEBUG: cyan + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: bold_red + format + reset,
        logging.CRITICAL: red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Logger():

    def __init__(self) -> None:
        
        self.logger = logging.getLogger('epm')
        self.logger.setLevel(logging.DEBUG)

        # create console handler with a higher log level

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(CustomFormatter())

        self.logger.addHandler(ch)
        
    def info(self ,message):
        
        self.logger.info(message)

    def debug(self ,message):
        
        self.logger.debug(message)

    def warning(self ,message):

        self.logger.warning(message)

    def error(self ,message):

        self.logger.error(message)

    def critical(self ,message):
        
        self.logger.critical(message)

    def exception(self ,message):

        self.logger.exception(message)

