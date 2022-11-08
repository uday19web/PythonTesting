from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get('https://rahulshettyacademy.com/client')

''' for using the LinkText locator - make sure the Tag in HTML mention in "anchor tag" <a>
in the LinkText - there are 2 ways 1. LinkText, 2. Partial Link Text - means half text of linktext
'''

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()

''' selecting XPATH locator by using the tags, like parent to child tags
ex - //form/div[1]/input'''
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

# for password using the tag name
driver.find_element(By.XPATH, " //form/div[2]/input").send_keys("Hello@12345")

''' Selecting CSS Selector locator by using the tags
the difference is remove slash into space for CSS Selector
ex - form div:nth-child(3) input'''
# to conform password
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Hello@12345")

# submit button
''' constructing the Xpath for 'text' for no anchor link in the tag'''
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
