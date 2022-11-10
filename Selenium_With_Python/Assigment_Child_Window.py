
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

''' for switch to child window we need to names of the window
we can find by using window handles'''
windowopens = driver.window_handles

#*******************************************************************************
'''switch to method used to switch the control to new window'''
driver.switch_to.window(windowopens[1])
text_list = driver.find_elements(By.XPATH, "//p[@class='im-para red']")
text = ''
mail = ''
for i in text_list:
    text = i.text.split()
for i in text:
    if "@" in i:
        mail = i
# closing the child window
driver.close()
#*******************************************************************************
# switch back to parent window
driver.switch_to.window(windowopens[0])
# find the email text box
driver.find_element(By.ID, "username").send_keys(mail)
# find the password text box
driver.find_element(By.ID, "password").send_keys("12345@Rahul")

#*******************************************************************************
# alert pop up
options = driver.find_elements(By.XPATH, "//span[@class='radiotextsty']")

for opt in options:
    if opt.text == "Admin":
        opt.click()
        break
#*******************************************************************************
# selecting Teacher
driver.find_element(By.XPATH, "//select[@class='form-control']").click()

form = driver.find_elements(By.XPATH, "//select[@class='form-control']/option")
# print(len(form))

for i in form:
    if i.text == "Consultant":
        i.click()
        break
###############################################
# Click the checkbox of terms and conditions
driver.find_element(By.CSS_SELECTOR, "#terms").click()
####################################
# click the sign in button
driver.find_element(By.ID, "signInBtn").click()
#########################
# catching the alert message
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

driver.close()



