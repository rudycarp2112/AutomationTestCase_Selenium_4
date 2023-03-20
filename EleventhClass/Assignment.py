import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://testautomationpractice.blogspot.com") # Play with de UI elements
driverChrome.maximize_window()

act=ActionChains(driverChrome)

#Double click
txt1=driverChrome.find_element(By.ID,"field1")
txt1.clear()
txt1.send_keys("Franco Rudy")
txt2=driverChrome.find_element(By.ID,"field2")
btn=driverChrome.find_element(By.XPATH,"(//button[normalize-space()='Copy Text'])[1]")
act.double_click(btn).perform()

time.sleep(4)

#Drag and drop
element=driverChrome.find_element(By.ID,"draggable")
target=driverChrome.find_element(By.ID,"droppable")

act.drag_and_drop(element,target).perform()

time.sleep(4)

#Drag and drop images
mrJhon=driverChrome.find_element(By.XPATH,"(//li[@class='ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle'])[1]")
mrsMary=driverChrome.find_element(By.XPATH,"(//li[@class='ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle'])[2]")
trashZone=driverChrome.find_element(By.ID,"trash")

act.drag_and_drop(mrJhon,trashZone).perform()
time.sleep(4)
act.drag_and_drop(mrsMary,trashZone).perform()

time.sleep(4)

#Slider
slider=driverChrome.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
position=slider.location
print("Position before move it: " + str(position))
act.drag_and_drop_by_offset(slider,200,0).perform()
position=slider.location
print("Position after move it: " + str(position))

time.sleep(4)
driverChrome.close()