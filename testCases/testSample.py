from utilities.customLogger import LogGen


def logs():
    logger = LogGen.loggen()
    logger.info("Info test")
