import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# In this 2 type of scenarios (download and upload files) its recommend not use selenium because is so many settings that not configured by automatization. Then, its recommend
# apply manual testing

currentLocation=os.getcwd() #return the absolute path to the current location

def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    preferences={"download.default_directory":currentLocation,
                 "plugins.always_open_pdf_externally":True} # key:value this configuration its stored in dictionary of python
    options= webdriver.ChromeOptions()
    options.add_experimental_option("prefs",preferences)
    driverChrome = webdriver.Chrome(service=servObj, options=options) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()

# ------------------ Chrome Driver

driverC.get("https://www.foundit.in")
driverC.maximize_window()
driverC.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
time.sleep(3)
driverC.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\Franco\FotosCV\CV_Resume.pdf") #Upload the file (i specify the path to the file)
btnSubmit=driverC.find_element(By.XPATH, "//input[@id='pop_upload']")

if btnSubmit.is_enabled()==True:
    print("File upload correctly")

print("Test passed")


driverC.close()
