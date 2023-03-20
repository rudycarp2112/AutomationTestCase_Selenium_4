import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #We need to import this for to select the options in DDL

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://itera-qa.azurewebsites.net/home/automation")
driverChrome.maximize_window()

# DDL it is self one webElement and correspong to the SELECT tag. Every option is a WebElement.
Travel_ddl_webElement=driverChrome.find_element(By.XPATH, value="//select[@class='custom-select']")
Travel_ddl=Select(Travel_ddl_webElement)

#Select an option (using built-in function)
Travel_ddl.select_by_visible_text("Spain") #Most of case is used
time.sleep(3)
Travel_ddl.select_by_value("7") # Malta. Usually not use because it can hapenning that the value and de Visible Text are the same so not need especify of this manner
time.sleep(3)
Travel_ddl.select_by_index("9") #Denmark. Start with 0.
time.sleep(3)

# Capture all options and print them
allOptions=Travel_ddl.options #Options become a webElement in array

for option in allOptions:
    print(option.text)

print("Total number of options: ", len(allOptions))
print("Test Passed")

#Select option from DDL without buil-in methods
# for option in allOptions:
#     if option.text=="Spain":
#         option.click()
#         break

#Find total number of options without Select
all_options=driverChrome.find_elements(By.XPATH, value="//select[@class='custom-select']//option")
print("All options: ", len(all_options))

time.sleep(3)