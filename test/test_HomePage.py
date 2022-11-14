import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageobject.homepage import HomePage
from ultilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getdata):
        # self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        log = self.getlogger()

        homepage = HomePage(self.driver)
        homepage.getemail().send_keys(getdata["Lastname"])
        homepage.getpassword().send_keys('1231414')
        homepage.getcheckbox().click()
        log.info("First name is " + getdata["Firstname"])
        homepage.getname().send_keys(getdata["Firstname"])
        homepage.empstatus().click()
        self.select_option(homepage.getgender(), getdata["gender"])
        homepage.getsubmit().click()
        message = homepage.getmessage().text
        assert ("Success" in message)
        self.driver.refresh()

    # this params entered in the field without refresh the webpage
    # so we can add refresh method if test case in the same webpage
    # or again we need to add the webpage url
    @pytest.fixture(params=HomePageData.gettestdata("Testcase2"))
    def getdata(self, request):
        return request.param

