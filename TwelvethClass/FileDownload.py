import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os

currentLocation=os.getcwd() #return the absolute path to the current location

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    preferences={"download.default_directory":currentLocation} # key:value this configuration its stored in dictionary of python
    options=webdriver.ChromeOptions()
    options.add_experimental_option("prefs",preferences)
    driverChrome = webdriver.Chrome(service=servObj,options=options) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

def edge_setup():
    from selenium.webdriver.edge.service import Service
    servObj = Service("C:\Pycharm2023\webdriver\msedgedriver")
    # Download files in desired location
    preferences = {"download.default_directory": currentLocation,
                 "plugins.always_open_msword_externally":True}  # key:value this configuration its stored in dictionary of python
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preferences)
    driverEdge = webdriver.Edge(service=servObj,options=options)
    driverEdge.implicitly_wait(10)

    return driverEdge

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    servObj = Service("C:\Pycharm2023\webdriver\geckodriver.exe")
    # Configured the manner to download the file
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") # Allow to download a particular type of file (MIME type)
    options.set_preference("browser.download.manager.showWhenStarting", False) # Allow to disable the emergent new windows which appear during before start download the file
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" # necessary to locate firefox .exe
    # Download files in desired location
    options.set_preference("browser.download.folderList", 2) # 0: download into desktop, 1: download in the default location (downloads folder) and 2: download in the desire location
    options.set_preference("browser.download.dir", currentLocation)
    driverFirefox = webdriver.Firefox(service=servObj,options=options)
    driverFirefox.implicitly_wait(10)

    return driverFirefox

# driverC=chrome_setup()
driverE=edge_setup()
# driverF=firefox_setup()

# ------------------ Chrome Driver

# driverC.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driverC.maximize_window()
# driverC.find_element(By.XPATH,"(//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file'])[1]").click()

# ------------------ Edge Driver (not run because when it perform the button a new windows is open and its not possible to locate de download button)

driverE.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driverE.maximize_window()
driverE.find_element(By.XPATH,"(//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file'])[1]").click()


# time.sleep(240)
time.sleep(7)
# iframe1=driverE.find_element(By.ID,"wacframe")
# driverE.switch_to.frame(iframe1)
# driverE.find_element(By.XPATH,"//button[@aria-label='Descargar']").click()

# ------------------ Firefox Driver

# driverF.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driverF.maximize_window()
# driverF.find_element(By.XPATH,"(//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file'])[1]").click()
#
# # Do this for close google ads window
# driverF.switch_to.frame(driverF.find_element(By.ID,"aswift_3"))
# driverF.switch_to.frame(driverF.find_element(By.ID,"ad_iframe"))
# driverF.find_element(By.XPATH,"//div[@id='dismiss-button']").click()

#Time for download the file example
# time.sleep(6)

# driverC.close()
driverE.close()
# driverF.close()