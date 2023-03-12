import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\msedgedriver")
driverChrome=webdriver.Edge(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driverChrome.maximize_window()

driverChrome.switch_to.frame("iframeResult")
txtOne=driverChrome.find_element(By.ID, value="field1")
txtTwo=driverChrome.find_element(By.ID, value="field2")
btnCopy=driverChrome.find_element(By.XPATH, value="//button[normalize-space()='Copy Text']")

txtOne.clear()
txtOne.send_keys("Franco")

act=ActionChains(driverChrome)
act.double_click(btnCopy).perform()

time.sleep(4)
driverChrome.close()