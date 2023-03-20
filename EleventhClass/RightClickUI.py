import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driverChrome.maximize_window()

btn=driverChrome.find_element(By.XPATH, value="//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driverChrome)
act.context_click(btn).perform()

time.sleep(4)

driverChrome.find_element(By.XPATH,"(//span[normalize-space()='Copy'])[1]").click()
time.sleep(4)
driverChrome.switch_to.alert.accept()

driverChrome.close()