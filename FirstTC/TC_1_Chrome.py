# default python path: C:\Users\RudyX\AppData\Local\Programs\Python

# packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Specified webdriver location
# serv_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
# driverChrome=webdriver.Chrome(service=serv_obj)

# Selenium 4 - Chrome

# Without specified webdriver location
driverChrome=webdriver.Chrome()
driverChrome.get("https://www.google.com/?hl=es")

# options=Options()
# options.page_load_strategy='eager'
driverChrome.implicitly_wait(20)


driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.implicitly_wait(20)

txtUser = driverChrome.find_element(by=By.XPATH, value="//Input[@name='username']")
txtPass = driverChrome.find_element(by=By.XPATH, value="//Input[@name='password']")
btnLogin = driverChrome.find_element(by=By.XPATH, value="//button[@type='submit']")

txtUser.send_keys("Admin")
txtPass.send_keys("admin123")
btnLogin.click()

titlePage = driverChrome.title

if titlePage == "OrangeHRM":
    print("Test Passed")
else:
    print("Test Failed")

# Print the tittle of the page
print(titlePage)
driverChrome.quit()