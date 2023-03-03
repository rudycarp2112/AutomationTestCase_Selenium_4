# This type of table usually is recepting changes from others users, for this reason is dynamically and not hardcode
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\msedgedriver")
driverChrome=webdriver.Edge(service=servObj)
driverChrome.implicitly_wait(20)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.maximize_window()

# login in page
driverChrome.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
driverChrome.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
driverChrome.find_element(By.CSS_SELECTOR, value="button[type='submit']").click()

# Enter to the table
driverChrome.find_element(By.XPATH, value="//a[normalize-space()='Admin']").click()
driverChrome.find_element(By.XPATH, value="//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']").click() #//nav[@aria-label='Topbar Menu']//ul//li[1]/span/i
driverChrome.find_element(By.XPATH, value="//a[normalize-space()='Users']").click()

# Apply logic test to the table
# //div[@class='oxd-table-body']//div[@class='oxd-table-card'][1]//div[@class='oxd-table-cell oxd-padding-cell'][4]
numRows=len(driverChrome.find_elements(By.XPATH, value="//div[@class='oxd-table-body']//div[@class='oxd-table-card']"))
numCols=len(driverChrome.find_elements(By.XPATH, value="//div[@class='oxd-table-body']//div[@class='oxd-table-card'][1]//div[@class='oxd-table-cell oxd-padding-cell']"))

print("Total number of rows: ", numRows)
print("Total number of cols: ", numCols)
count=0

for row in range(1, numRows+1):
    status=driverChrome.find_element(By.XPATH, value="//div[@class='oxd-table-body']//div[@class='oxd-table-card']["+str(row)+"]//div[@class='oxd-table-cell oxd-padding-cell'][5]").text
    if status=="Enabled":
        count+=1

print("Total number of enabled users: ", count)
print("Test Passed")
driverChrome.close()