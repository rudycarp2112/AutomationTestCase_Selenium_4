import logging

# logger = logging.getLogger()
# fhandler = logging.FileHandler(filename='C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Logs\\Reporter.log', mode="a")
# formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# fhandler.setFormatter(formatter)
# fhandler.setLevel(logging.INFO)
# logger.addHandler(fhandler)
# logger.info("Information Message")
# logger.warning("Information Message")
# logger.debug("Information Message")
# logger.error("Information Message")
#
# print("Archivo creado")

# Example to create a log file

import logging

logger = logging.getLogger()
formatter = logging.Formatter(
    "[%(asctime)s][%(name)s][%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
)
file_handler = logging.FileHandler("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Logs\\demo project.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
# stream_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

logger.info("info message")