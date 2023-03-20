# is a popup which is come from the browser, not from de Web Application
# we cant by pass to this popup and we cant make inyection in this popup

# before create webdriver object need specify options before to perform the web driver
import time
from selenium import webdriver
from selenium import Service

opts= webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj, options=opts)
driverChrome.implicitly_wait(10)

driverChrome.get("https://whatmylocation.com")
driverChrome.maximize_window()

time.sleep(10)