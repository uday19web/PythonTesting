import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

''' Implicitly wait" - used to tell the script to wait the object to show in the webpage
maximum of mentioned seconds ana object 2 sec la show agiduchina it till proceed the script
Implicityly wait applicable to all lines in the code no need use Sleep'''
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# selecting search box
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

'''where we are using the "find elements" - to return type list there implicitly wait 
will not work there we have to use time.sleep(). because selenium will not check the list
contains values or not. It check only the return type.
This is only exception for implicitly wait methods.'''

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
''' "Chaining" - means we continue the parent element to child
results obj la upto //div[@class='products']/div ithu varaikum namba capture panitom
irukura product add kudu ka namba ithula iruthu continue pananum in for loop'''

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

######## next page
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)


driver.close()