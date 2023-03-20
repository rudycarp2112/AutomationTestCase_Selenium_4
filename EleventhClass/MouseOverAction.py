# Its about keeping the mouse arrow on a dropdown of options
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\msedgedriver")
driverChrome=webdriver.Edge(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()

# login in page
driverChrome.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
driverChrome.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
driverChrome.find_element(By.CSS_SELECTOR, value="button[type='submit']").click()

# Enter to the table
adminMenu=driverChrome.find_element(By.XPATH, value="//a[normalize-space()='Admin']")
managementMenu=driverChrome.find_element(By.XPATH, value="//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']")
usersOption=driverChrome.find_element(By.XPATH, value="//a[normalize-space()='Users']")

# To perform mouse over action (first import a package and we need create a object of class)
act=ActionChains(driverChrome)
# Whole statement just create an action
act.move_to_element(adminMenu).move_to_element(managementMenu).move_to_element(usersOption).click().perform()

time.sleep(4)
driverChrome.close()

# ActionChains
# 1) MouseOver   move_to_element(element)
# 2) Right click context_click(element)
# 3) Double click double_click(element)
# 4) Drag and Drop   drag_and_drop(element)