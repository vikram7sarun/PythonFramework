import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://SeleniumLogs//test.log",
                            format='%(asctime)s:  %(levelname)s: %(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

