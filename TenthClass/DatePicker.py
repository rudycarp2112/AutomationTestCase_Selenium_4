# There are two types of web Elements:
# - Standard: Are those wich usually are present in all pages with the same type of web Elementa and can reconize without problems for automation script
# - Not Standard: Are those wich are present in pages and sometimes can be diferent kind of single webElements as DatetimePicker and can to cause the automation script must be re-design
# to read the kin of webElement. Are customized webElements for the developers.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(20)

driverChrome.get("https://jqueryui.com/datepicker/")
driverChrome.maximize_window()

# Switch to iframe
driverChrome.switch_to.frame(0)

# Send date directly
# driverChrome.find_element(By.XPATH, value="(//input[@id='datepicker'])[1]").send_keys("16/09/1998") #format: dd/mm/yyyy

# Select date manually (because are diferent kinds of dateTimePicker)
year="1998"
month="September"
date="16"

# Open dtp
driverChrome.find_element(By.XPATH, value="(//input[@id='datepicker'])[1]").click()

# Select Month and year
while True:
    currentMonth=driverChrome.find_element(By.XPATH, value="//span[@class='ui-datepicker-month']").text
    currentYear=driverChrome.find_element(By.XPATH, value="//span[@class='ui-datepicker-year']").text
    if year==currentYear and month==currentMonth:
        break
    else:
        driverChrome.find_element(By.XPATH, value="(//a[@title='Prev'])[1]").click()

# Select date
datesOfMonth=driverChrome.find_elements(By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
datesOfMonth[int(date)-1].click()

print(int(date))

time.sleep(4)

print("Test Passed")