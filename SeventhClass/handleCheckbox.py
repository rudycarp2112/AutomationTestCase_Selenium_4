import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://itera-qa.azurewebsites.net/home/automation")
driverChrome.maximize_window()

# 1) select 1 checkbox
# driverChrome.find_element(By.ID, value="monday").click()

# 2) select all the checkboxes
dayOfWeek_ck=driverChrome.find_elements(By.XPATH, value="//input[@type='checkbox' and contains(@id, 'day')]")

# Approach 1
for daysOfWeek in dayOfWeek_ck:
    daysOfWeek.click()

# Approach 2
# for i in range(len(dayOfWeek_ck)):
#     dayOfWeek_ck[i].click()

# 3) select only two checkboxes of choice
# for i in range(2):
#     dayOfWeek_ck[i].click()

# 4) select the last two checkboxes
# for i in range(len(dayOfWeek_ck)-2, len(dayOfWeek_ck)):
#     dayOfWeek_ck[i].click()

# 5) select the first two checkboxes
# for i in range(len(dayOfWeek_ck)):
#     if i<2:
#         dayOfWeek_ck[i].click()

# 6) uncheck the checkboxes than was selected previosuly (is_selected)
time.sleep(5)
for i in dayOfWeek_ck:
    if i.is_selected():
        i.click()

time.sleep(5)
driverChrome.close()
print("Test Passed")