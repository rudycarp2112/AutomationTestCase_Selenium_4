# Broken links always will be greater or equal to 400
# normal links always less than 400, we can say that responds an error on response code (they having propers resources in web server)
# to diferentiate them we need to validate which are broken and normal. This can be done trough the Request Module of python (should be installed). This is API testing, not web Testing.

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("http://www.deadlinkcity.com")
driverChrome.maximize_window()

allLinks=driverChrome.find_elements(By.TAG_NAME, value="a")
count=0

for link in allLinks:
    url=link.get_attribute("href")
    try:
        response=requests.head(url)
    except:
        None # Sometimes the response obtained from the server to client bring exceptions related to network, for avoid this we can handle through try-except

    if response.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is valid link")

print(count, " total number of broken links in web page")