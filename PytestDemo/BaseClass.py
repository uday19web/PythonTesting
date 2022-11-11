import inspect
import logging


class BaseClass:


    def getlogger(self):
        # this will give correct file name other wise in log file name will be BaseClass
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(__name__)s : %(message)s")
        filehandler.setFormatter(formatter)  # connecting the formatter, filehandler to add handler

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger
