from selenium.webdriver.common.by import By

from pageobject.checkoutpage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    password = (By.ID, 'exampleInputPassword1')
    boxcheck = (By.ID, 'exampleCheck1')
    name = (By.CSS_SELECTOR, "input[name='name']")
    employsta = (By.CSS_SELECTOR,'#inlineRadio1')
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, 'alert-success')

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkpage = CheckOutPage(self.driver)
        return checkpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.boxcheck)

    def empstatus(self):
        return self.driver.find_element(*HomePage.employsta)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getmessage(self):
        return self.driver.find_element(*HomePage.message)