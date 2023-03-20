import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as EC #Import to handle Exception with Explicit_Wait
from selenium.webdriver.support.select import Select # Import to manipulate options in DDL
from selenium.webdriver.chrome.options import Options
import requests # Import to request resource to the webserver based on a URL

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

# driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()

# we logged in the page
# driverChrome.find_element(By.NAME, value="username").send_keys("Admin")
# driverChrome.find_element(By.NAME, value="password").send_keys("admin123")
# driverChrome.find_element(By.CSS_SELECTOR, value="button[type='submit']").submit()

def printAllOptions(ddlOptions, description):
    for option in ddlOptions:
        print(option.text + " - " + description)

    print("Number of total options: ", len(ddlOptions))

#Search for all links in the homePage
# allLinksHome=driverChrome.find_elements(By.TAG_NAME, value="a")
#
# print("Total number of links: ", len(allLinksHome))
# for links in allLinksHome:
#     url=links.get_attribute("href")
#     print(url)

# Determinate if there are valid links or broken links
# for links in allLinksHome:
#     url = links.get_attribute("href")
#     try:
#         response=requests.head(url)
#     except:
#         None
#     if response.status_code >= 400:
#         print(url, "is correct link. CODE: " + str(response.status_code))
#     else:
#         print(url, "is broken link")
#
# # access to one link
# for link in allLinksHome:
#     if link.text=="Time":
#         link.click()
#         break
#
# time.sleep(3)
# print("Test 1 Passed")

# driverChrome.get("https://testautomationpractice.blogspot.com")

# Play with the options of radioButton (soon)


# Play with the options of DDL
# ddlSpeedWebElement=driverChrome.find_element(By.NAME, value="speed")
# ddlSpeed=Select(ddlSpeedWebElement)
# ddlSpeedAllOptions=ddlSpeed.options
#
# printAllOptions(ddlSpeedAllOptions, "DDL Speed")
#
# ddlSpeed.select_by_visible_text("Faster")
#
# # print option selected
# optSelected=ddlSpeed.first_selected_option
# print("Option selected: " + optSelected.text + "\n")
#
# ddlNumberWebElement=driverChrome.find_element(By.NAME, value="number")
# ddlNumber=Select(ddlNumberWebElement)
# ddlNumberOptions=ddlNumber.options
#
# printAllOptions(ddlNumberOptions, "DDL Number")
#
# ddlNumber.select_by_index(3)
#
# # print option selected
# optSelected=ddlNumber.first_selected_option
# print("Option selected: " + optSelected.text + "\n")
#
# ddlAnimalsWebElement=driverChrome.find_element(By.ID, value="animals")
# ddlAnimals=Select(ddlAnimalsWebElement)
# ddlAnimalsOptions=ddlAnimals.options
#
# printAllOptions(ddlAnimalsOptions, "DDL Animals")
#
# ddlAnimals.select_by_value("babycat")
#
# # print option selected
# optSelected=ddlAnimals.first_selected_option
# print("Option selected: " + optSelected.text + "\n")
#
# time.sleep(3)

# Play with the options of CheckBox
driverChrome.get("https://itera-qa.azurewebsites.net/home/automation")

ckbTools=driverChrome.find_elements(By.XPATH, value="//div[@class='custom-control custom-checkbox']/child::label") #Its important to verify if checkbox option is enable, bring the input
# tag that contain the attribute. For this case, label is webElement separate from input, so, to check de attribute ENABLE it's advisible consult such as LABEL as INPUT tag

#In this case only have been use the LABEL tag for each checkbox
count=0
for opt in ckbTools:
    if opt.text!="None":
        print("Options Enable to select - FOR: " + str(opt.get_attribute("for")))
        count+=1

print("Total number of options: ", count)

#Selet an specific option
for i in range(len(ckbTools)):
    if ckbTools[i].get_attribute("for")=="serenity":
        ckbTools[i].click()
        break

time.sleep(3)

#Unselect the option select previously
for i in range(len(ckbTools)):
    if ckbTools[i].is_selected():
        ckbTools[i].click()
        break

time.sleep(3)

print("Test Passed")
driverChrome.close()
