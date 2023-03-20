# they search fix the synchronization between application web and the code of automatization TC
# this ocurrs due to velocity aspects of the application web or network response instead of control de web Aaplication we can control automatization schemes

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By
from selenium import WebDriverWait, expected_conditions as EC  # import this
from selenium import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException # and this

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
# driverWaitExplicit=WebDriverWait(driverChrome,10) #basic sintax to declare explicit wait
driverWaitExplicit=WebDriverWait(driverChrome,10,poll_frequency=2.5,ignored_exceptions=[NoSuchElementException, #poll_frecuency only specified for each certain time the script needs to call the statement newly
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception]) # To ignore all type of exceptions

driverChrome.get("https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwiQ04TtmK79AhWuqJUCHUJHBSkQPAgI")
driverChrome.maximize_window()

txtSearch=driverChrome.find_element(By.NAME, value="q")
txtSearch.send_keys("selenium")
txtSearch.submit()

linkWebSelenium=driverWaitExplicit.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))) # there are more functions based on different conditions.
linkWebSelenium.click()

# Explicit wait its based on the conditions but not based on the time, the time is only spicified the time to wait then the webElement is not available.
# If the condition not ocurrs, after a few seconds, then the script continue with the next statement

# Advantage
# 1) More effectively works.
# 2) Its use in big proyects where the time of execution needs to be more eficient
# 3) Allow handled the execeptions if the webElement fails the condition

# Disadvantage
# 1) Should be called in multiple places where we need to use explicit_waits
# 2) For people feel some difficulty