# isnt a webElement, its a special element. We cant identify any element in alert window.
# We must create an object of type alert from webdriver and switch on it

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

# driverChrome.get("https://the-internet.herokuapp.com/javascript_alerts")
driverChrome.get("https://mypage.rediff.com")
driverChrome.maximize_window()

# driverChrome.find_element(By.CSS_SELECTOR, value="button[onclick='jsPrompt()']").click()
#
# alertWindow=driverChrome.switch_to.alert
#
# print(alertWindow.text)
#
# alertWindow.send_keys("Selenium 4")
#
# # alertWindow.accept()
# alertWindow.dismiss()
#
# time.sleep(3)

driverChrome.find_element(By.XPATH, value="//input[contains(@value,'Go')]").click()

time.sleep(3)

driverChrome.switch_to.alert.accept() # automatically closed alert instead of created an object
# alertWindow.accept()

print("TC passed")

driverChrome.close()