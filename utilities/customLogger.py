import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="/home/anonymous/PycharmProjects/QAtask-WADIC/Report/automation.logs", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
