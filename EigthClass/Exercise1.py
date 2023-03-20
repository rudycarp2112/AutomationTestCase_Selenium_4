# Exercise 1: open multiple windows and close all them
import time
from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://testautomationpractice.blogspot.com")
driverChrome.maximize_window()

# Access the links
driverChrome.find_element(By.CSS_SELECTOR, value="#Wikipedia1_wikipedia-search-input").send_keys("selenium")
driverChrome.find_element(By.CSS_SELECTOR, value="input[type='submit']").submit()

allResults=driverChrome.find_elements(By.XPATH, value="//div[@id='Wikipedia1_wikipedia-search-results']//a")

# Open windows based of resultd obtained
for link in allResults:
    link.click()

# print tittles of webPage
windows=driverChrome.window_handles

for window in windows:
    driverChrome.switch_to.window(window)
    print("Tittle of webPage: "+driverChrome.title+ "- ID: " +str(window))

# position in first window (1 of 6)
driverChrome.switch_to.window(windows[0])

time.sleep(5)

# close all windows
driverChrome.quit()
