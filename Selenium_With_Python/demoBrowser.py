from selenium import webdriver
from selenium.webdriver.chrome.service import Service

'''chrome browser
# we cant invoke the chrome browser directly
# we need use "chrome driver" to use proxy driver
service_obj = Service(r'D:\Python\Chrome_diver\chromedriver')

driver = webdriver.Chrome(service=service_obj)
'''

'''
# this for firefox
service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')

driver = webdriver.Firefox(service=service_obj)
'''

# for Edge browser
service_obj = Service(r'D:\Python\Edge\msedgedriver')

driver = webdriver.Edge(service=service_obj)


# to maximise the window
driver.maximize_window()

# to visit which website want land
driver.get('https://rahulshettyacademy.com')

# to see the title of the tab
print(driver.title)

# to get current url at that moment the browser launched
print(driver.current_url)

driver.get('https://courses.rahulshettyacademy.com/p/python-sdet-automation-testing')

# to minimise the window
driver.minimize_window()
# to go back in the url
driver.back()

# to refresh the webpage
driver.refresh()

# to go forward in the webpage
driver.forward()

driver.close()