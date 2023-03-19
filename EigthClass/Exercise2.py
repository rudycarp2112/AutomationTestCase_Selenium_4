# Exercise 2: access a form and complete the input text use switch_to.frame(value index)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://testautomationpractice.blogspot.com")
driverChrome.maximize_window()

iframeVonlunteerSignUp=driverChrome.find_element(By.XPATH, value="//iframe[@id='frame-one1434677811']")
driverChrome.switch_to.frame(iframeVonlunteerSignUp)

# complete data
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-1']").send_keys("Franco")
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-2']").send_keys("Rudy")
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-3']").send_keys("3513416791")
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-4']").send_keys("Argentina")
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-5']").send_keys("Cordoba")
driverChrome.find_element(By.XPATH, value="//input[@id='RESULT_TextField-6']").send_keys("franco.rudy@hotmail.com")

#Select Gender
driverChrome.find_element(By.CSS_SELECTOR, value="label[for='RESULT_RadioButton-7_0']").click()

# Mark days of i available
checkBoxOptions=driverChrome.find_elements(By.XPATH, value="//label[contains(@for, 'RESULT_CheckBox')]")

for option in checkBoxOptions:
    if option.text=="Monday" or option.text=="Tuesday" or option.text=="Wednesday" or option.text=="Thursday" or option.text=="Friday":
        option.click()
        time.sleep(2)

# Specific time of contact
ddlTimeContact=driverChrome.find_element(By.XPATH, value="//select[@id='RESULT_RadioButton-9']")
optionsTimeContact=Select(ddlTimeContact)
optionsTimeContact.select_by_visible_text("Afternoon")

time.sleep(5)
#Send form
driverChrome.find_element(By.XPATH, value="//input[@id='FSsubmit']").submit()

time.sleep(5)

print("Test Passed")
driverChrome.close()