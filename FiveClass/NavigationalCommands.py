import time

from selenium import webdriver
from selenium import Service

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

driverChrome.get("https://www.frc.utn.edu.ar")

driverChrome.back()
time.sleep(3)
driverChrome.forward()
time.sleep(3)
driverChrome.refresh()

driverChrome.quit()

# aplication, broser and navigational commands are aply to Driver