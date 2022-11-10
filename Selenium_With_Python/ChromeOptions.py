from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

'''we can invoke the behaviour of the browser using ChromeOptions in Webdriver'''
chrome_options = webdriver.ChromeOptions()
'''we can add all the argument and then we can invoke the browser
check "chrome option python" in google
some websites are - https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions'''
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="D:\Python\Chrome_diver\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(2)
print(driver.title)