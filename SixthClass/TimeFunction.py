import time

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)

driverChrome.get("https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwiQ04TtmK79AhWuqJUCHUJHBSkQPAgI")
driverChrome.maximize_window()

txtSearch=driverChrome.find_element(By.NAME, value="q")
txtSearch.send_keys("selenium")
txtSearch.submit()

time.sleep(5)
driverChrome.find_element(By.XPATH, value="//h3[text()='Selenium']").click()

# problem with the stop times in the script:
#     1) performance of the script is very poor most of times
#     2) If the element is not available within the time mentioned, still there is a chance of getting an exception
# this function only works with the script, not with webElements. Its simple to use.