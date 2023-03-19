import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://demos.jquerymobile.com/1.4.2/rangeslider/")
driverChrome.maximize_window()

# In this type of webElement, ever we need to find a manner that allow me to have a position reference into the slider.
# For those case, we can suppose a x and y axis position respect at one webElement that we can move with de cursor. This manner we can plus or minus value to it position.

min_slider=driverChrome.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/a[1]")
max_slider=driverChrome.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/a[2]")

print("Location of minimum slider before moving: " + str(min_slider.location)) #{'x': 1080, 'y': 410}
print("Location of maximum slider before moving: " + str(max_slider.location)) #{'x': 1535, 'y': 410}

time.sleep(4)
act=ActionChains(driverChrome)
act.drag_and_drop_by_offset(min_slider, 200, 0).perform() # x=-455 for the slider go to 0
act.drag_and_drop_by_offset(max_slider, -100, 0).perform()

print("Location of minimum slider after moving: " + str(min_slider.location)) #{'x': 1284, 'y': 410}
print("Location of maximum slider after moving: " + str(max_slider.location)) #{'x': 1432, 'y': 410}

time.sleep(3)

# its normal that the result of positions after we move it are not the same that we expected. for example, the value of x axis in the min_slider is expected that equal to 1280 but
# we see that there are a diference for 4 units. Because depends is most of case that de application resolution.

driverChrome.close()