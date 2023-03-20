# there are 3 types of links: broken links, external links and internal links.
# broken links are those that do not redirect anywhere, dont have any target page (as result are displayed error codes or error warning: 401 ex.)
# external link are those that redirect a diferent web page
# internal links are those that redirect to others parts of the webpage
from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://demo.nopcommerce.com/login?returnUrl=%2F/home/automation")
driverChrome.maximize_window()

# 1) click on one link
# driverChrome.find_element(By.LINK_TEXT, value="Digital Downloads").click()
# driverChrome.find_element(By.PARTIAL_LINK_TEXT, value="Digital").click()

# 2) bring all the links of webPage
lks=driverChrome.find_elements(By.TAG_NAME, value="a")
# lks=.driverChrome.find_elements(By.XPATH, value="//a")

for i in lks:
    print(i.text) # There are some links that not print in console because not have one attribute "HREF" to redirect. For those we should handle bronken links.

print("Test Passed")