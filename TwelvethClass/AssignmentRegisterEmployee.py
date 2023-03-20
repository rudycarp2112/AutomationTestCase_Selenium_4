import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium import Select

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

# Enter at the page
driverC.get("https://demo.automationtesting.in/Register.html")
driverC.maximize_window()

# Complete textbox
driverC.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Franco")
driverC.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Rudy")
driverC.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("Davila Adolfo 715")
driverC.find_element(By.XPATH,"//input[@type='email']").send_keys("franco.rudy@hotmail.com")
driverC.find_element(By.XPATH,"//input[@type='tel']").send_keys("5493513416791")
driverC.find_element(By.XPATH,"//input[@value='Male']").click()

#select hobby (radiobtn)
ckbHobbies=driverC.find_elements(By.XPATH,"//input[@type='checkbox']")
for opt in ckbHobbies:
    if opt.get_attribute("value")=="Hockey":
        opt.click()
        break
#Select Language
divLanguage=driverC.find_element(By.XPATH,"//div[@class='col-md-4 col-xs-4 col-sm-4']//multi-select").click()
ddlLanguage=driverC.find_elements(By.XPATH,"//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']//li")
time.sleep(2)
for opt in ddlLanguage:
    if opt.text=="Spanish" or opt.text=="English":
        opt.click()
        print(opt.text)

#Select Skills
ddlSkills=driverC.find_element(By.XPATH,"//select[@id='Skills']")
ddlSkillsOptions=Select(ddlSkills)
ddlSkillsOptions.select_by_value("Javascript")
time.sleep(1)

#Select Country
ddlCountries=driverC.find_element(By.XPATH,"//span[@class='select2-selection select2-selection--single']").click()
ddlCountriesOptions=driverC.find_elements(By.XPATH,"//ul[@id='select2-country-results']//li")
for opt in ddlCountriesOptions:
    if opt.text=="South Africa":
        opt.click()
        break


time.sleep(1)
# Set date of birth
ddlYear=driverC.find_element(By.XPATH,"//select[@id='yearbox']")
ddlYearOptions=Select(ddlYear)
ddlYearOptions.select_by_visible_text("1998")


ddlMonth=driverC.find_element(By.XPATH,"//select[@placeholder='Month']")
ddlMonthOptions=Select(ddlMonth)
ddlMonthOptions.select_by_visible_text("September")

ddlDay=driverC.find_element(By.XPATH,"//select[@id='daybox']")
ddlDayOptions=Select(ddlDay)
ddlDayOptions.select_by_visible_text("16")

driverC.find_element(By.XPATH,"//input[@id='firstpassword']").send_keys("Lenny2023")
driverC.find_element(By.XPATH,"//input[@id='secondpassword']").send_keys("Lenny2023")

# Upload file
time.sleep(2)
driverC.find_element(By.XPATH,"//input[@id='imagesrc']").send_keys("C:\Franco\FotosCV\Buena2.jpg")

if driverC.find_element(By.XPATH,"//input[@id='imagesrc']").text=="buena2":
    print("Image uploaded")

# Submit form
time.sleep(3)
driverC.find_element(By.XPATH,"//button[@id='submitbtn']").click()

print("Test Passed")

driverC.close()