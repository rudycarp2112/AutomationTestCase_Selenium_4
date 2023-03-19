import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(20)

driverChrome.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driverChrome.maximize_window()

#Open dtp
driverChrome.find_element(By.NAME, value="dob").click()

#select month
dtpMonth=driverChrome.find_element(By.XPATH, value="//select[@aria-label='Select month']")
dtpDllMonth=Select(dtpMonth)

dtpDllMonth.select_by_visible_text("Sep")

#select year
dtpYear=driverChrome.find_element(By.XPATH, value="//select[@aria-label='Select year']")
dtpDllYear=Select(dtpYear)

dtpDllYear.select_by_visible_text("1998")

#select date
dates=driverChrome.find_elements(By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text=="16":
        date.click()
        break

time.sleep(4)
print("Test Passed")