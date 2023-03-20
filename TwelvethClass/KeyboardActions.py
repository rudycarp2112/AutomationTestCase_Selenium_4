import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://text-compare.com")
driverChrome.maximize_window()

act=ActionChains(driverChrome)

# Actions:
# CTRL+E
# CTRL+C
# TAB
# CTRL+V

txtBox1=driverChrome.find_element(By.NAME,"text1")
txtBox2=driverChrome.find_element(By.NAME,"text2")

txtBox1.clear()
txtBox1.send_keys("A day with my friend Pavan")

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #key_down: press the keyboard key, key_up: release the keyboard key
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)

driverChrome.close()