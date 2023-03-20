import time
from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driverChrome.maximize_window()

# Its normal that iframes inside a webPage or another webPage. In this case, we cant access to the elements directly. So we need to switch into it for interact
# with this elements

# THis would display an error because the three webElements are in diferentes Iframes and not can be accesible. "Unable to locate element".
# Before we to perform any activity we need to switch to the iframe
# driverChrome.find_element(By.LINK_TEXT, value="org.openqa.selenium.chrome").click()
# driverChrome.find_element(By.LINK_TEXT, value="ChromeDriver").click()
# driverChrome.find_element(By.LINK_TEXT, value="Help").click()

#Manners of access iframe (form, frame or iframe) (selenium 4):
# * driverChrome.switch_to.frame("name of frame")
# * driverChrome.switch_to.frame("id of frame")
# * driverChrome.switch_to.frame(webElement frame)
# * driverChrome.switch_to.frame(index) (if not have index then access starting 0)

driverChrome.switch_to.frame("packageListFrame")
driverChrome.find_element(By.LINK_TEXT, value="org.openqa.selenium.chrome").click()
driverChrome.switch_to.default_content() #go back to the main Page


driverChrome.switch_to.frame("packageFrame") # webDriver cant directly switch to another frame, before we need to go back to a main page
driverChrome.find_element(By.LINK_TEXT, value="ChromeDriver").click()
driverChrome.switch_to.default_content()

driverChrome.switch_to.frame("classFrame")
driverChrome.find_element(By.XPATH, value="//div[@class='topNav']//a[normalize-space()='Help']").click()

time.sleep(3)

driverChrome.close()