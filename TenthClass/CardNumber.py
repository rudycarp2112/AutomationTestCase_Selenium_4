import time

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driverChrome.maximize_window()

time.sleep(5)
driverChrome.find_element(By.XPATH, value="//input[@id='payment_method_yith-stripe']").click()

time.sleep(5)
# IframeCardNumber=driverChrome.find_element(By.XPATH, value="(//p[@class='form-row form-row-last woocommerce-validated'])[1]/div[@id='yith-stripe-card-number']/div[@class='__PrivateStripeElement']/iframe[@title='Secure card number input frame']")
form1=driverChrome.find_element(By.XPATH, value="//form[@name='checkout']")
driverChrome.switch_to.frame(form1)
# formNumCard_2=driverChrome.find_element(By.XPATH, value="//form[@class='ElementsApp is-empty']")
# driverChrome.switch_to.frame(iframeNumCard_1)
# driverChrome.switch_to.frame(formNumCard_2)
driverChrome.find_element(By.XPATH, value="//div[@class='CardNumberField CardNumberField--ltr']/div[@class='CardNumberField-input-wrapper']/input").send_keys("4545 4545 4545 4545")
driverChrome.switch_to.default_content()
