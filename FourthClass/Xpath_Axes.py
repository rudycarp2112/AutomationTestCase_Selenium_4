from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# page: https://money.rediff.com/gainers
# video: https://youtu.be/XL2pU5y3Kf8?list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&t=1865

serv_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome=webdriver.Chrome(service=serv_obj)

driverChrome.get("https://money.rediff.com/gainers")
driverChrome.maximize_window()

# reference self element
# txtMsg=driverChrome.find_element(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/self::a").text
# print(txtMsg)

# reference parent element
# txtMsg=driverChrome.find_element(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/parent::td").text
# print(txtMsg)

# reference childs elements
# childs=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/child::td")
# print("number of childs: " + str(len(childs))) #5

# reference ancestor element
# txtMsg=driverChrome.find_element(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr").text
# print(txtMsg) # Aurum Proptech B 116.80 128.45 + 9.97 (return the value of all elements in the TR row)

# reference descendant element
# descendants=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/descendant::*")
# print(len(descendants))
#
# for i in descendants:
#     print(i.text) # There are 7 descendants because some nodes are compounds of TD, A and FONT tags

# reference following element
# followings=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/following::*")
# print(len(followings)) # 11223 following

# reference following-sibling element
# followingSiblings=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/following-sibling::*")
# print("Number of following siblings:"+str(len(followingSiblings))) # 1358 following siblings

# reference preceding element
# precedings=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/preceding::*")
# print(len(precedings)) # 338 following

# reference preceding-sibling element
followingSiblings=driverChrome.find_elements(By.XPATH, value="//a[contains(text(),'Aurum Proptech')]/ancestor::tr/preceding-sibling::tr")
print("Number of preceding siblings:"+str(len(followingSiblings))) # 23 preceding siblings

# Diferences between preceding-siblings or folowing-siblings and preceding or following
# preceding-siblings find out paralel nodes of DOM that correspond to beyond nodes (top of page) and have the same hierarchy.
# The same apply to following siblings but from the above (bottom of page)
# the following and preceding find out that elements or nodes that are in bottom or top of web page correspondly no matter the hierarchy