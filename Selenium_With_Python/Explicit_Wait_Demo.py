import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

''' Implicitly wait" - used to tell the script to wait the object to show in the webpage
maximum of mentioned seconds ana object 2 sec la show agiduchina it till proceed the script
Implicityly wait applicable to all lines in the code no need use Sleep'''
driver.implicitly_wait(2)

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

# list of vegetables
expected_veglist = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
# print("lenght of expected veg list is {}".format(len(expected_veglist)))
exp_veg = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_veg = []
for veg in expected_veglist:
    actual_veg.append(veg.text)
print(actual_veg)
assert exp_veg == actual_veg

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = int(price.text) + sum

totalamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert totalamt == sum



######## next page
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

''' explictly wait - used to overwrite the implicitly wait in a particular cases.
yena all thing will show in 5 sec but some it will more time if it is showing that is issue in
the applications.
for that we need to import some package to use explicitly wait'''

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

# check discount amount is less than total

discountamt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
# print("Discount AMT is {}".format(discountamt))

assert totalamt > discountamt



driver.close()
