from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)

driverChrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driverChrome.implicitly_wait(20)
driverChrome.maximize_window()

# Login
txtUser=driverChrome.find_element(by=By.CSS_SELECTOR, value="input[placeholder='Username']").send_keys("Admin")
txtPwd=driverChrome.find_element(by=By.XPATH, value="//input[@name='password']").send_keys("admin123")
btnLogin=driverChrome.find_element(by=By.CSS_SELECTOR, value="button.oxd-button").click() #button.oxd-button

#Home
tittlePage=driverChrome.title
if tittlePage=="OrangeHRM":
    print("User logged")
else:
    print("User not logged")

optionsMenu=driverChrome.find_elements(By.CLASS_NAME, value="oxd-main-menu-item-wrapper")
print("There are: " + str(len(optionsMenu)) + " options")

#Filter User from PIM in page
btnPIM=driverChrome.find_element(By.LINK_TEXT, value="PIM").click()

# txtNameUser=driverChrome.find_elements(By.CSS_SELECTOR, value="input[data-v-7c56a434]")
# txtNameUser[0].send_keys("Kevin")

txtNameUser=driverChrome.find_element(By.XPATH, value="(//input[@placeholder='Type for hints...'])[1]").send_keys("Kevin")

# txtIdUser=driverChrome.find_elements(By.CSS_SELECTOR, value="input[data-v-844e87dc]")
# txtIdUser[1].send_keys("0058")

txtIdUser=driverChrome.find_element(By.XPATH, value="(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("0058")

btnSearchUser=driverChrome.find_element(By.CSS_SELECTOR, value="button[type=submit]").click()

#Verify the user filtred (next class)

rowKevin=driverChrome.find_element(By.XPATH, value="//div[contains(text(),'0058')]") # With this sentence i only recovered the element DIV, so, i need verify the text that contains
print(rowKevin.text)
assert rowKevin.text=="0058"

print("Test Passed")


