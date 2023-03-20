import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# when i launch my browser it remember some data. Ej: username or password for a specific web page. Browser can remember this information in form of cookies
# this cookies are temporaly files which are created by the browser whenever browse some web site. some browser are restricted and others can create it.
# if i have deleted all information about cookies in the browser i just go to browser settings and delete them.
# through selenium we can extract information of cookies once the browser is launched (name, expire date, etc). See if the cookies are created or not.
# we can create our own cookie when you initalize the broser.
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj)
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()
driverC.get("https://demo.nopcommerce.com")
driverC.maximize_window()

# get cookies that are created for WEB APP (will capture cookies from the browser).
# A cookie isnt a web element. Is a object with attributes which it have some value. With de sintax: [key:value]
# 1 cookie of information can storage in dictionary object
chromeCookies=driverC.get_cookies()
print("Number of cookies: ", len(chromeCookies))

for i in chromeCookies:
    # print(i)
    print(i.get("name")+" : "+ i.get("value"))

# Add a new cookie to the browser. We have to specify the cookie with the dictionary format. The cookies may have 2 or more attributes.
driverC.add_cookie({"name":"MyCookie","value":"7777777"})
chromeCookies=driverC.get_cookies()
print("Number of cookies adding new one: ", len(chromeCookies)) # Some browser maybe not allow to create cookies

# Delete specific cookie form the browser
driverC.delete_cookie("MyCookie")
chromeCookies=driverC.get_cookies()
print("Number of cookies once deleted one: ", len(chromeCookies))

# Delete all cookies
driverC.delete_all_cookies()
chromeCookies=driverC.get_cookies()
print("Number of cookies once deleted one: ", len(chromeCookies))

# sometimes browsing a web APP and get the cookies maybe not return the same value because the websites are dynamic. Our intentions is only adding or deleted a specific cookie.
# Is rarely use cookies in testing for a proyect.

driverC.close()