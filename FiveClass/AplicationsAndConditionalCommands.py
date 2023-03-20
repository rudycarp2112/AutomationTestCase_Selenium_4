from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)

driverChrome.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

# There are many methods that can be divided in caterories:

# applications commands

# print(driverChrome.title) # to capture the tittle of current webPage
# print(driverChrome.current_url) # to capture the URL of the current webPage
# print(driverChrome.page_source) # to capture the code of DOM of the current webPage

# conditional commands its importants to test the webPage. Return true or false. This methods only can access through WebElements.

# is_displayed: to verify if the webElement is available in the current webPage

displayTxtEmail=driverChrome.find_element(By.XPATH, value="//input[@id='Email']").is_displayed()
print("Display status: "+str(displayTxtEmail))

# is_enabled: to verify if the webElement is available to interact (input text, to click, etc) with it in the current webPage

enableTxtMail=driverChrome.find_element(By.XPATH, value="//input[@id='Email']").is_enabled()
print("Enable status: "+ str(enableTxtMail))

driverChrome.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# is_selected: to verify if the webElement (such as radio button, checkbox, inputs) is selected in the current webPage
rbtn_male=driverChrome.find_element(By.CSS_SELECTOR, value="#gender-male")
rbtn_female=driverChrome.find_element(By.CSS_SELECTOR, value="#gender-female")

print("Status radio buttons before one of them is selected: ")
print("Status rdButton Male: "+ str(rbtn_male.is_selected()))
print("Status rdButton Female: "+ str(rbtn_female.is_selected()))

rbtn_male.click()

print("Status radio buttons after one of them is selected (male): ")
print("Status rdButton Male: "+ str(rbtn_male.is_selected()))
print("Status rdButton Female: "+ str(rbtn_female.is_selected()))

rbtn_female.click()

print("Status radio buttons after one of them is selected (female): ")
print("Status rdButton Male: "+ str(rbtn_male.is_selected()))
print("Status rdButton Female: "+ str(rbtn_female.is_selected()))

