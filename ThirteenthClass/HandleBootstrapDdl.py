import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Select

# If the web Element is not defined with select tag then create a list that saved of li tags  and go through it with a loop until detecting the element that you want to select
def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()
driverC.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driverC.maximize_window()

driverC.find_element(By.XPATH,"//p[@id='billing_country_field']//span[@class='woocommerce-input-wrapper']").click()
countryDdl=driverC.find_element(By.XPATH,"//select[@id='billing_country']")
countryDdlOptions=Select(countryDdl)

countryDdlOptions.select_by_visible_text("Antigua and Barbuda")

time.sleep(4)

print("Test Passed")
driverC.close()