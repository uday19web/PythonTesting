from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)

# click on the column header
driver.find_element(By.XPATH, '//span[text()="Veg/fruit name"]').click()

'''we check the locators by using browser console
syntax - $x("//tr/td[1]" - it will highlight the selected web element in browser'''
# collect all veggieList -> veggieList
vegetables = driver.find_elements(By.XPATH, "//tr/td[1]")
webveglist = []
for veg in vegetables:
    webveglist.append(veg.text)

'''we have to copy list into new list. we can use slice or copy. copy is faster than slice'''
orginalsortedlist = webveglist.copy()
print(orginalsortedlist)
# Sort this veggieList -> newsortedList
'''if we sorted list we cant able save in newlist because it will sort in collected list also
due to tha we are saving the list into one variable'''
webveglist.sort()
print(webveglist)
# check Veggielist == NewSortedList
assert webveglist == orginalsortedlist