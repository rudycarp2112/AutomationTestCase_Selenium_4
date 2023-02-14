# Test Case
# installation python path: C:\Users\RudyX\AppData\Local\Programs\Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Specified webdriver location
# serv_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
# driverChrome=webdriver.Chrome(service=serv_obj)

# Without specified webdriver location
driverChrome=webdriver.Chrome()
driverChrome.get("https://www.google.com/?hl=es")

# options=Options()
# options.page_load_strategy='eager'
driverChrome.implicitly_wait(20)

# Opcion 1 ----------------------------------------
# txtSearch = driverChrome.find_element(by=By.NAME, value="q")
# btnSearch = driverChrome.find_element(by=By.NAME, value="btnK")
#
# txtSearch.send_keys("Maroon 5")
# btnSearch.click()
#
# print(driverChrome.title)

# Opcion 2 ----------------------------------------
driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.implicitly_wait(20)

txtUser = driverChrome.find_element(by=By.XPATH, value="//Input[@name='username']")
txtPass = driverChrome.find_element(by=By.XPATH, value="//Input[@name='password']")
btnLogin = driverChrome.find_element(by=By.XPATH, value="//button[@type='submit']")

txtUser.send_keys("Maroon 5")
txtPass.send_keys("Admin")
btnLogin.click()

# Print the tittle of the page
print(driverChrome.title)