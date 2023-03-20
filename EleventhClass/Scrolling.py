import time
from selenium import webdriver
from selenium import Service

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://www.worldometers.info/geography/flags-of-the-world/")
driverChrome.maximize_window()

# This action not depends of the web application, is a property of the browser windows so to use it we dont need call the ActionChains class. However its a mouse operation.

# 1. Scroll down page by pixel
# driverChrome.execute_script("window.scrollBy(0,3000)","")
# valueScroll=driverChrome.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", valueScroll)

# 2. Scroll down page till the element is visible
# flagNorway=driverChrome.find_element(By.XPATH,"(//img[@src='/img/flags/small/tn_no-flag.gif'])[1]")
# driverChrome.execute_script("arguments[0].scrollIntoView();", flagNorway)
# valueScroll=driverChrome.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", valueScroll) #6981

# 3. Scroll down page till the end of webPage
driverChrome.execute_script("window.scrollBy(0,document.body.scrollHeight)")
valueScroll=driverChrome.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", valueScroll) #10485
time.sleep(3)
driverChrome.execute_script("window.scrollBy(0,-document.body.scrollHeight)") # To back to starting point
valueScroll=driverChrome.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", valueScroll) #0

time.sleep(5)

# The scroll is only controlled by JS statements

driverChrome.close()