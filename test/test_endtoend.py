from selenium.webdriver.common.by import By


from pageobject.homepage import HomePage
from ultilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()

        homepage = HomePage(self.driver)
        checkpage = homepage.shopitems()

        log.info("Getting all the card titles")

        products = checkpage.getcardtitle()
        print(len(products))

        for ele in products:
            productname = ele.find_element(By.XPATH, "div/h4/a").text
            log.info(productname)
            if productname == "Blackberry":
                ele.find_element(By.XPATH, 'div/button').click()
                break

        # click the checkout button
        checkpage.getcardfooter().click()

        # Next page checkout button
        conformpage = checkpage.clicksuccessbutton()
        log.info("Entering country name as ind")

        # next page country search box
        conformpage.searchcountry().send_keys("ind")

        self.verifylinkpresence("India")
        # click on India
        conformpage.country().click()
        # checkbox click
        conformpage.checkbox().click()

        # purchase button
        conformpage.purchase().click()
        # grab the sucess message
        text = conformpage.grabmessage().text
        log.info("Text received from application is " + text)

        assert "Success! Thank you!" in text


