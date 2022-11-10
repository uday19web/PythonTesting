from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r'D:\Python\Firefox_Driver\64\geckodriver')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# click the shop button
''' using locator as "href"
 syntax: css - "a[href*='shop']", xpath - //a[contains(@href, 'stop')]
 first of all dont use regular expression. If no way the use regexp in Css'''

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # href '*' - refers regular expression

##############################################
# to find the blackberry
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(products))

for ele in products:
    productname = ele.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        ele.find_element(By.XPATH, 'div/button').click()
        break

# click the checkout button
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

# Next page checkout button
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

# next page country search box
driver.find_element(By.ID, "country").send_keys("ind")
'''explicit wait'''
wait = WebDriverWait(driver, 10)
# wait until link text showing
# complete web element and locator in one bracket otherwise it will through error
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

# click on India
driver.find_element(By.LINK_TEXT, "India").click()
# checkbox click
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
# purchase button
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# grab the sucess message
text = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in text

driver.close()
