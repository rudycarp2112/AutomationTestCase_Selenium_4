# they search fix the synchronization between application web and the code of automatization TC
# this ocurrs due to velocity aspects of the application web or network response instead of control de web Aaplication we can control automatization schemes

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10) #seconds. If the application webPage dosent respond within this time the we should report this as a performance bug to the team

driverChrome.get("https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwiQ04TtmK79AhWuqJUCHUJHBSkQPAgI")
driverChrome.maximize_window()

txtSearch=driverChrome.find_element(By.NAME, value="q")
txtSearch.send_keys("selenium")
txtSearch.submit()

driverChrome.find_element(By.XPATH, value="//h3[text()='Selenium']").click()

# implicit_wait() allow with only one statement to wait the script until the webElement is available within the time specified. Soon as soon is available, the next
# statement will to perform instead of wait the total time in seconds.
# This function is a process that running in parallel with webDrvier, so will execute for another statements until the driver its close.


# Advantage
# 1) Single statement
# 2) Performance not will reduced (if the element is available within the time it proceed to execute further statements)
#
# Disadvantage
# 1) If the element is not available within the time mentioned still there is a chance of getting an exception (not handle exception and aply the same time wait to all statements)