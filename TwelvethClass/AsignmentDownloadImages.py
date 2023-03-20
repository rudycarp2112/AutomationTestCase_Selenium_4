import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# https://docs.testproject.io/articles/Help%20Articles/Using%20Chrome%20Profile%20with%20Selenium%20Desired%20capabilities%20-%20Autologin%20&%20Permissions
currentLocation=os.getcwd() #return the absolute path to the current location

def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    preferences={"download.default_directory":currentLocation,
                 "plugins.always_open_jpg_externally":True} # key:value this configuration its stored in dictionary of python
    options= webdriver.ChromeOptions()
    options.add_experimental_option("prefs",preferences)
    driverChrome = webdriver.Chrome(service=servObj, options=options) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()
driverC.get("https://file-examples.com/index.php/sample-images-download/sample-jpg-download/")
driverC.maximize_window()
driverC.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click() # it's not downloaded beause instead to inicialice the download a new windows is open and display the image
# The problem can be fixed adding a new preference statement to the options variable.
time.sleep(10)