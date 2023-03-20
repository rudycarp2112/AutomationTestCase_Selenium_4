import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)

driverChrome.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

############### find_element return one webelement

# Locator matching with one element
# txtSearch=driverChrome.find_element(By.XPATH, value="//input[@id='small-searchterms']")
# txtSearch.send_keys("Iphone")
# time.sleep(3)
# Locator matching with multiple elements
# linksFooter=driverChrome.find_element(By.XPATH, value="//div[@class='footer']//a")
# print(linksFooter.text)
# time.sleep(3)
# Locator matching with one element but its not available. This cant do because not return a WebElement. as result throw the SuchNoElement Exception
# linkRegister=driverChrome.find_element(By.LINK_TEXT, value="Regis")
# linkRegister.click()

############### find_elements return multiple webelements as LIST COLLECTION OBJECT

# Locator matching with one element
txtSearch=driverChrome.find_elements(By.XPATH, value="//input[@id='small-searchterms']")
txtSearch[0].send_keys("Iphone")
time.sleep(3)

# Locator matching with multiple elements
linksFooter=driverChrome.find_elements(By.XPATH, value="//div[@class='footer']//a")
for i in linksFooter:
    print(i.text)
time.sleep(3)

# Locator matching with one element but its not available. With FIND_ELEMENTS not throw the SuchNoElement Exception, for default return a empty list collection
linkRegister=driverChrome.find_elements(By.LINK_TEXT, value="Regis")
print(str(len(linkRegister)))

