from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')

'''
locators that supported by selenium are 
Id, Xpath, CSSselector, Classname, name, LinkText
'''
# send keys are used to type the text in the locators
driver.find_element(By.NAME, 'email').send_keys('hello@gmail. com')

# locate the password box by "id"
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456adfsadf')


# locate the check box
driver.find_element(By.ID, 'exampleCheck1').click()
'''
except Xpath, CSS selector are not our hand because these are created by developers
But we can construct the Xpath, CSS Selector to identify the locator.
'''

# Syntax for CSS Selector
# tagname[attribute='value'] -> input[name='name']
# other ways Css Selector is -
#   #id using id, using dot by class name - .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Uday')
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

#######################################
# Static Drop down
''' if you see the select tag in Html that one is "static dropdown" - we need use "Select Class" 
to handle it. 3 Ways we can handle the static dropdown menu
1. select by visible text, 2. select by index, 3.select by value - value added in the html'''
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value()

####################################

# difference between Css Selector and Xpath is double slash "//" and "@"
'''
 syntax for Xpath
 Xpath = //tagname[@attribute='value'] -> //input[@type='submit']
 <input class="btn btn-success" type="submit" value="Submit"> in inspect element in browser
 '''
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# if the "class" have separated by space those are individual class name
# ex - <div class="alert alert-success alert-dismissible"></div>

# text - for retrieve the message what shown after hit the submit button
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

# to check the message is correct or not
assert "Success" in message

''' if you find multiple xpath locator we can use index to select the particular Xpath'''
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")

# to clear the text typed by using 'Clear'
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()