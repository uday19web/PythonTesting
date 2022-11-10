from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

'''window handles are used to return the what are the windows open in browser as list'''
windowopen = driver.window_handles
print(windowopen)
'''for switch to the new window we need to use switch to'''
# this will move the selenium control to child window
driver.switch_to.window(windowopen[1])
# using tagname as locator
print(driver.find_element(By.TAG_NAME, "h3").text)
# this will close the child tab
driver.close()
# this will move the control to parent window
driver.switch_to.window(windowopen[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text