import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

# Its recommend whenever some TC fail we capture the error and serve as envidence for the developer
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj)
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()
driverC.get("https://demo.nopcommerce.com")
driverC.maximize_window()

# i want to access to register form but in a new tab in the browser

# old Approach in python (this manner i continue focus on the first tab)
# registerLink=Keys.CONTROL+Keys.RETURN
# driverC.find_element(By.LINK_TEXT,"Register").send_keys(registerLink) # This just works in chrome browser, for every browser are different type of shortcuts

# new Approach in python (switch to a new tab)
# driverC.switch_to.new_window("tab") # it will open a new tab and switch into it (selenium 4)
# driverC.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# new Approach in python (switch to a new browser window)
driverC.switch_to.new_window("window") # it will open a new window and switch into it (selenium 4)
driverC.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
driverC.quit()