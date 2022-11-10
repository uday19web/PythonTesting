from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://the-internet.herokuapp.com/iframe")

'''for switch to frames we need "switch_to.frame(give the frame id or name)" '''
driver.switch_to.frame("mce_0_ifr")

# to clear the text the field
driver.find_element(By.ID, "tinymce").clear()

driver.find_element(By.ID, "tinymce").send_keys("I am able to automate the frames")

'''how to switch from frames to browser
by using the "default content" - means where the selenium intiated it will come there'''
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)

driver.close()

