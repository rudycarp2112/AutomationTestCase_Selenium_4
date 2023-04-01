import logging

class LogGeneration:
    @staticmethod
    def Loggen():
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        fhandler = logging.FileHandler(filename='C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Logs\\automation.log')
        fhandler.setFormatter(formatter)

        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO) # With this sentence i can print the message type INFO, ERROR and WARNING
        # logger.setLevel(logging.DEBUG) # If we want to logged the bug type sentences from the console then we can show them with this line (its a lot of lines)
        logger.info("-----> Execution of TC")
        return logger

    def msgInfoLogFile(self, comment):
        self.info("************************ " + comment + " ************************")
        return self

    def msgErrorLogFile(self, comment):
        self.error("************************ " + comment + " ************************")
        return self

    def msgWarningLogFile(self, comment):
        self.warning("************************ " + comment + " ************************")
        return self

