from selenium.webdriver.common.by import By

from pageobject.conformpage import ConformPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardtitle = (By.XPATH, "//div[@class='card h-100']")
    cardfooter = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    sucessbutton = (By.CSS_SELECTOR, ".btn-success")

    def getcardtitle(self):
        # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # * is to tell it is a tuple format to python
        return self.driver.find_elements(*self.cardtitle)

    def getcardfooter(self):
        return self.driver.find_element(*self.cardfooter)

    def clicksuccessbutton(self):
        self.driver.find_element(*self.sucessbutton).click()
        conformpage = ConformPage(self.driver)
        return conformpage
