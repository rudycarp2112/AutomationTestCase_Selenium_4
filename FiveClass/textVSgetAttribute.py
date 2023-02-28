import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)

driverChrome.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

txtMail=driverChrome.find_element(By.XPATH, value="//input[@id='Email']")
print(txtMail.text)

txtMail.clear()
txtMail.send_keys("franco.rudy@gmail.com")

print("Result of text: "+txtMail.text) # Not print nothing BECAUSE text() only bring INNER TEXT (text from the TAG)
print("Result of get_Attributte: "+txtMail.get_attribute("value")) # return values of any attribute of web element (value, id, class)

# now we will do the same but for a button
btnLogin=driverChrome.find_element(By.XPATH, value="//button[normalize-space()='Log in']")

print("Result of text (button): "+btnLogin.text)
print("Result of get_Attributte (button): "+btnLogin.get_attribute("value")) #not printed nothing because this webElement dont have text, only Inner Text
print("Result of get_Attributte (button): "+btnLogin.get_attribute("class"))
