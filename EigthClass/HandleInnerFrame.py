#Its a Frame that contains another frame
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://demo.automationtesting.in/Frames.html")
driverChrome.maximize_window()

#Display inner frame on page
driverChrome.find_element(By.XPATH, value="//a[normalize-space()='Iframe with in an Iframe']").click()

#Enter to outer frame
outerFrame=driverChrome.find_element(By.XPATH, value="//iframe[@src='MultipleFrames.html']")
driverChrome.switch_to.frame(outerFrame)

#Enter to inner frame
innerFrame=driverChrome.find_element(By.XPATH, value="//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driverChrome.switch_to.frame(innerFrame)

#Identify input box an write some stuff
driverChrome.find_element(By.CSS_SELECTOR, value="input[type='text']").send_keys("You're welcome")
time.sleep(3)

# go to the parent frame (outter frame)
driverChrome.switch_to.parent_frame()

#go to the main page
driverChrome.switch_to.default_content()

driverChrome.close()