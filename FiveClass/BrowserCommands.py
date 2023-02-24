import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

driverChrome.find_element(By.LINK_TEXT, value="OrangeHRM, Inc").click()

time.sleep(5)

driverChrome.close() #quit() close multiple browser windows beacuse kill the Chrome Driver Process. Each tab windows is a diferente process.

time.sleep(5)

# we can see that the close command only close one tab browser this happening because the driver only focused in one aplication browser, not in the second one that open
# this one difference with quit command. Another difference is that this command close one aplication browser but not finish the thread process open for driver



