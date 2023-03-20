# https://youtu.be/4DHefIyw6ik?list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&t=1970

from selenium import webdriver
from selenium import Options

options = Options()
options_page_load_strategy= "normal"
webdriverChrome= webdriver.Chrome(options=options)

webdriverChrome.get("https://demo.nopcommerce.com")
webdriverChrome.maximize_window()

## Unique SecondClass_Locators
# locators to find one element (more of time) - properties: ID, NAME, LINK_TEXT, PARTIAL_LINK_TEXT
# webdriverChrome.find_element(By.ID, value="small-searchterms").send_keys("galaxy")
# webdriverChrome.find_element(By.NAME, value="q").send_keys("galaxy")
# webdriverChrome.find_element(By.LINK_TEXT, value="Register").click()
# webdriverChrome.find_element(By.PARTIAL_LINK_TEXT, value="ister").click()

# locators to find one or MORE elements (more of time, example: five radio buttons)
# slides = webdriverChrome.find_elements(By.CLASS_NAME, value="nivo-imageLink")
# print(len(slides))  # 2 total images

# links = webdriverChrome.find_elements(By.TAG_NAME, value="a")
# print(len(links)) # 90 total links

## Customized SecondClass_Locators

# CSS_SELECTOR
# XPATH

print(webdriverChrome.title)

#webdriverChrome.close() # close one of all webdrivers open
#webdriverChrome.quit() # all webdrivers open