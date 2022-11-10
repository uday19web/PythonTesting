from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Uday"
service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

''' alert pop ups are not written in Html- it is written in Java or Javascript
selenium can automate only the HTML'''

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

''' we need switch the browser mode to alert mode to check the popups.
alert object is only focus on the alert it will not have any focus on browser level.'''
alert = driver.switch_to.alert

# to grab the text in alert message using "Text"
alert_text = alert.text
print(alert_text)

# to make our text is enter in the alert message
assert name in alert_text

''' in the alert there two methods 1. Positive, 2. Negative.
Positive means "Accept", Negative means "dismiss" 
alert.accetp() - positive, alert.dismiss() - negative'''
alert.accept()