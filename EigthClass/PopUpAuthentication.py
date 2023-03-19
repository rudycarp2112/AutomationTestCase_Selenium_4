# Before you access an web application web browser must to authenticade if you are a legitim user (only happening in companies)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

# driverChrome.get("https://the-internet.herokuapp.com/basic_auth/basic_auth")
driverChrome.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driverChrome.maximize_window()

time.sleep(4)

# for to passed the data required to the pop up we need to use injection syntax on URL (is the only way we can access this type of applications)

# URL: https://the-internet.herokuapp.com/basic_auth/basic_auth
# Syntax: https://username:password@test.com
# Example: https://admin:admin@the-internet.herokuapp.com/basic_auth

driverChrome.close()

#we have to inyect de username and password in the URL
