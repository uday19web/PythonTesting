import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:

    def getlogger(self):
        # this will give correct file name other wise in log file name will be BaseClass
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler("logfile.log", mode='w')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(__name__)s : %(message)s")
        filehandler.setFormatter(formatter)  # connecting the formatter, filehandler to add handler

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        return logger

    def verifylinkpresence(self, text):
        '''explicit wait'''
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option(self, locator, text):

        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)