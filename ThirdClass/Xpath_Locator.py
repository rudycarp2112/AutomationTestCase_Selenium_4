# https://youtu.be/79zNHoiCKw4?list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&t=4452

# Absolute path starts from root html node
# Absolute path starts with one slash
# Absolute path only we use tags/nodes

# Relative Xpath directly jump to element on DOM with certain ID or attribute
# Relative Xpath starts with two slash
# Relative Xpath only we use attributes

#both use more time of processing
# selectors hub is a extension for browsers that generate several locators for one we element, is most popular. This allow waste a lot fo effort

# there are 2 reason to prefer relative xpath:
# 1)  Because when the developer introduce new elements then absolute path will be broken because the DOM change
# 2) If developer change the location of the elements then absolute path will be broken
#
# Absolute Xpath is unstable

# -------------------------------------------------------------------------------------------------------------------------------- Xpath Options

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=serv_obj)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()
driverChrome.implicitly_wait(20)

# absolute Xpath
# driverChrome.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin")
# driverChrome.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin123")
# driverChrome.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()

# relative Xpath
# driverChrome.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
# driverChrome.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
# driverChrome.find_element(By.XPATH, value="//button[@type='submit']").click()

# OR
# driverChrome.find_element(By.XPATH, value="//input[@placeholder='Usernamess' or @name='username']").send_keys("Admin")
# driverChrome.find_element(By.XPATH, value="//input[@placeholder='Password' and @name='password']").send_keys("admin123")
# driverChrome.find_element(By.XPATH, value="//button[@type='submit']").click()

# start-with() and contain() functions
# driverChrome.find_element(By.XPATH, value="//input[starts-with(@placeholder, 'User')]").send_keys("Admin")
# driverChrome.find_element(By.XPATH, value="//input[contains(@type, 'ord')]").send_keys("admin123")
# driverChrome.find_element(By.XPATH, value="//button[starts-with(@type, 'subm')]").click()

# text()
driverChrome.find_element(By.XPATH, value="//p[text()='Forgot your password? ']").click()

print("Test Passed")