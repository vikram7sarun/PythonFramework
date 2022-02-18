import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s:  %(levelname)s: %(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

