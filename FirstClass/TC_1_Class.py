# default python path: C:\Users\RudyX\AppData\Local\Programs\Python

# packages
from selenium import webdriver
from selenium.webdriver.common.by import By

# Specified webdriver location
# serv_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
# driverChrome=webdriver.Chrome(service=serv_obj)

# Selenium 4 - Chrome

# options=Options()
# options.page_load_strategy='eager'
# driverChrome.implicitly_wait(20)

executeTC = 2

if executeTC==1:
    # Without specified webdriver location
    driverChrome = webdriver.Chrome()

    driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driverChrome.implicitly_wait(20)

    txtUser = driverChrome.find_element(by=By.XPATH, value="//Input[@name='username']")
    txtPass = driverChrome.find_element(by=By.XPATH, value="//Input[@name='password']")
    btnLogin = driverChrome.find_element(by=By.XPATH, value="//button[@type='submit']")

    txtUser.send_keys("Admin")
    txtPass.send_keys("admin123")
    btnLogin.click()

    titlePage = driverChrome.title
    if titlePage == "OrangeHRM":
        print("Test Passed")
    else:
        print("Test Failed")
    driverChrome.quit()

elif executeTC==2:
    driverEdge = webdriver.Edge()

    driverEdge.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driverEdge.implicitly_wait(20)

    txtUser = driverEdge.find_element(by=By.XPATH, value="//Input[@name='username']")
    txtPass = driverEdge.find_element(by=By.XPATH, value="//Input[@name='password']")
    btnLogin = driverEdge.find_element(by=By.XPATH, value="//button[@type='submit']")

    txtUser.send_keys("Admin")
    txtPass.send_keys("admin123")
    btnLogin.click()

    titlePage = driverEdge.title
    if titlePage == "OrangeHRM":
        print("Test Passed")
    else:
        print("Test Failed")
    driverEdge.quit()
else:
    driverFirefox = webdriver.Firefox()

    driverFirefox.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driverFirefox.implicitly_wait(20)

    txtUser = driverFirefox.find_element(by=By.XPATH, value="//Input[@name='username']")
    txtPass = driverFirefox.find_element(by=By.XPATH, value="//Input[@name='password']")
    btnLogin = driverFirefox.find_element(by=By.XPATH, value="//button[@type='submit']")

    txtUser.send_keys("Admin")
    txtPass.send_keys("admin123")
    btnLogin.click()

    titlePage = driverFirefox.title
    if titlePage == "OrangeHRM":
        print("Test Passed")
    else:
        print("Test Failed")
    driverFirefox.quit()

# Print the tittle of the page
print(titlePage)