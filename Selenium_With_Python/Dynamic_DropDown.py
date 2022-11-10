import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
# for make script to wait we use time sleep
time.sleep(2)

'''find elements plural - stores all the element by the locators
find elements methods return the values as "list" '''

countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')
print(len(countries))
# print(countries) # it print the web element

for country in countries:
    # to retrieve web element in the list need to "text"
    if country.text == 'India':
        country.click()
        break # why break means we got the desired results no need run the loop unnecessarily

'''.text method is not working for the capture the dynamic drop down text because 
those text are not shown in the website on first time loaded'''
# print(driver.find_element(By.ID, "autosuggest").text) # this will return nothing

# for this we are using "get attribute"
assert driver.find_element(By.ID, "autosuggest").get_attribute('value') == "India"
