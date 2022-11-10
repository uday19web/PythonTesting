from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

'''Headless means - run the script in the backend we cant able to see the action'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") # need to give the argument in chrome webdriver as options

'''sometimes we will get the error or warning this website is harmful we use advanced to go webpage
for that we need give one more argument to selenium to understand'''
chrome_options.add_argument("--ignore-certificate-errors")


service_obj = Service(r'D:\Python\Chrome_diver\chromedriver')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")




'''got "Console" after right click inspect in the browser
as a tester mostly we use Scroll in the JS executor because sometimes the 
we element will be in the bottom of the webpage.
window.scrollBy(0, 500) - 500 is pixel height to scroll
window.scrollBy(0, document.body.scrollHeight) - it will scroll upto max height means to bottom of page'''

'''method called execute script that used to execute the Js
we need give in Js method so we used the semicolon at the end'''
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

'''we can also take screenshot in python it will with previous step'''
driver.get_screenshot_as_file("screen.png")


driver.close()