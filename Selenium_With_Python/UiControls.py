import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

################ check box #################
checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        ''' for check the checkbox is clicked we can use "is_selected" method - it return true or false'''
        assert checkbox.is_selected()
        break
#######################################################
######### Radio option ##############3
radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
'''when i know that position will not change in the webpage we no need to use the for loop'''
radiobutton[2].click()
assert radiobutton[2].is_selected()

''' using the "is_displayed" option - it will return true or false'''
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
'''after the hide the text it will not display so we using 'not' in assert to is_displayed 
showing false'''
assert not driver.find_element(By.ID, "displayed-text").is_displayed()







driver.close()

