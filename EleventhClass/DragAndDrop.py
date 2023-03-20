import time

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By
from selenium import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\msedgedriver")
driverChrome= webdriver.Edge(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driverChrome.maximize_window()

act=ActionChains(driverChrome)

source_rome=driverChrome.find_element(By.ID, "box6")
target_italy=driverChrome.find_element(By.ID, "box106")

source_washington=driverChrome.find_element(By.ID, "box3")
target_usa=driverChrome.find_element(By.ID, "box103")

act.drag_and_drop(source_rome,target_italy).perform()
act.drag_and_drop(source_washington,target_usa).perform()

time.sleep(4)
driverChrome.close()