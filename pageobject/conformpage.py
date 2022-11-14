from selenium.webdriver.common.by import By


class ConformPage:
    def __init__(self, driver):
        self.driver = driver

    countrysearch = (By.ID, "country")
    countryselect = (By.LINK_TEXT, "India")
    checkboxclick = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchasebutton = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def searchcountry(self):
        return self.driver.find_element(*self.countrysearch)

    def country(self):
        return self.driver.find_element(*self.countryselect)

    def checkbox(self):
        return self.driver.find_element(*self.checkboxclick)

    def purchase(self):
        return self.driver.find_element(*self.purchasebutton)

    def grabmessage(self):
        return self.driver.find_element(*self.message)
