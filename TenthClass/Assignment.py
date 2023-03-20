# Write automation code that completes the purchase of a ticket
import time

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By
from selenium import Select

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driverChrome.maximize_window()

# Choose ticket option to buy (through input tag, attribute id)
ckbTypeTicket=driverChrome.find_elements(By.XPATH, value="//ul[@id='checkout-products']/li/label/input")
for option in ckbTypeTicket:
    if option.get_attribute("id")=="product_3186":
        option.click()
        break
time.sleep(5)

# complete fields about passenger
driverChrome.find_element(By.NAME, value="travname").send_keys("Franco Ignacio")
driverChrome.find_element(By.NAME, value="travlastname").send_keys("Rudy")
driverChrome.find_element(By.ID, value="order_comments").send_keys("This is an exercise of automatization code")

# select date of birth
driverChrome.find_element(By.NAME, value="dob").click()
dtpMonth=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-month")
dtpMonthDdl=Select(dtpMonth)

dtpMonthDdl.select_by_visible_text("Sep")

dtpYear=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-year")
dtpYearDdl=Select(dtpYear)

dtpYearDdl.select_by_visible_text("1998")

dayOfBirth=16

daysOfMonth=driverChrome.find_elements(By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
daysOfMonth[dayOfBirth-1].click()
# select genre
genres=driverChrome.find_elements(By.XPATH, value="//input[contains(@id,'sex_')]")
for opt in genres:
    if opt.get_attribute("id")=="sex_1":
        opt.click()

# select type trip (round trip)
driverChrome.find_element(By.XPATH, value="//input[@id='traveltype_2']").click()

driverChrome.find_element(By.NAME, value="fromcity").send_keys("Argentina")
driverChrome.find_element(By.NAME, value="tocity").send_keys("Mexico")

#Select Date of Departure
DepartureYear="2023"
DepartureMonth="Apr"
DepartureDay=3

driverChrome.find_element(By.NAME, value="departon").click()

dtpMonth=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-month")
dtpMonthDdl=Select(dtpMonth)
dtpMonthDdl.select_by_visible_text(DepartureMonth)

dtpYear=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-year")
dtpYearDdl=Select(dtpYear)
dtpYearDdl.select_by_visible_text(DepartureYear)

daysOfMonth=driverChrome.find_elements(By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
daysOfMonth[DepartureDay-1].click()

#Select Date of Return
ReturnYear="2023"
ReturnMonth="Apr"
ReturnDay=10

driverChrome.find_element(By.NAME, value="returndate").click()

dtpMonth=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-month")
dtpMonthDdl=Select(dtpMonth)
dtpMonthDdl.select_by_visible_text(ReturnMonth)

dtpYear=driverChrome.find_element(By.CLASS_NAME, value="ui-datepicker-year")
dtpYearDdl=Select(dtpYear)
dtpYearDdl.select_by_visible_text(ReturnYear)

daysOfMonth=driverChrome.find_elements(By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
daysOfMonth[ReturnDay-1].click()

# select purpose of dummy ticket (dummy ticket and hotel)

ckbPurpose=driverChrome.find_element(By.XPATH, value="//select[@id='reasondummy']")
ckbPurposeOptions=Select(ckbPurpose)

ckbPurposeOptions.select_by_visible_text("Prank a friend")

# Select how to recieve the ticket
driverChrome.find_element(By.XPATH, value="(//input[@id='deliverymethod_2'])[1]").click()

# billing details
driverChrome.find_element(By.NAME, value="billname").send_keys("Aerolineas Argentinas")
driverChrome.find_element(By.NAME, value="billing_phone").send_keys("+54 351 341 6791")
driverChrome.find_element(By.NAME, value="billing_email").send_keys("franco.rudy@hotmail.com")

countryOptions=driverChrome.find_element(By.NAME, value="billing_country")
ddlCountryOptions=Select(countryOptions)

ddlCountryOptions.select_by_visible_text("Argentina")

driverChrome.find_element(By.NAME, value="billing_address_1").send_keys("Colon 2567")
driverChrome.find_element(By.NAME, value="billing_address_2").send_keys("Department B")
driverChrome.find_element(By.NAME, value="billing_city").send_keys("Cordoba")

countryOptions=driverChrome.find_element(By.NAME, value="billing_state")
ddlCountryOptions=Select(countryOptions)

ddlCountryOptions.select_by_visible_text("Córdoba")

driverChrome.find_element(By.NAME, value="billing_postcode").send_keys("6500")

# Verify order total
orderTotal=driverChrome.find_element(By.XPATH, value="//table[@class='shop_table woocommerce-checkout-review-order-table']/tfoot/tr[@class='order-total']/td/strong/span").text
moneySelectedOption=driverChrome.find_element(By.XPATH, value="(//span[@class='woocommerce-Price-amount amount'])[4]").text

print(orderTotal)
print(moneySelectedOption)

if orderTotal==moneySelectedOption:
    print("The order total is correct")

# select type of payment
time.sleep(5)
# ckbTypePayment=driverChrome.find_element(By.XPATH, value="(//input[@id='payment_method_yith-stripe'])[1]").click()
ckbTypePayment=driverChrome.find_elements(By.XPATH, value="//div[@id='payment']//ul[@class='wc_payment_methods payment_methods methods']/li/input")
for typePayment in ckbTypePayment:
    if typePayment.get_attribute("id")=="payment_method_yith-stripe":
        typePayment.click()
        print(typePayment.get_attribute("id"))
        break

time.sleep(2)
# complete card data
driverChrome.find_element(By.ID, value="yith-stripe-card-name").send_keys("Franco Rudy")
driverChrome.find_element(By.XPATH, value="//div[@id='yith-stripe-card-expiry']/div/input").send_keys("09/27")
# iframeExpiration=driverChrome.find_element(By.CSS_SELECTOR, value="iframe[title='Secure expiration date input frame']")
# driverChrome.switch_to.frame(iframeExpiration)
# driverChrome.find_element(By.ID, value="yith-stripe-card-expiry").send_keys("09/27")
# driverChrome.switch_to.default_content()
time.sleep(2)
# iframeNumCard_1=driverChrome.find_element(By.XPATH, value="//div[@id='yith-stripe-card-number']/div[@class='__PrivateStripeElement']/iframe[@name='__privateStripeFrame53063']")
formNumCard_2=driverChrome.find_element(By.XPATH, value="//form[@class='ElementsApp is-empty']")
# driverChrome.switch_to.frame(iframeNumCard_1)
driverChrome.switch_to.frame(formNumCard_2)
driverChrome.find_element(By.XPATH, value="//div[@class='CardNumberField CardNumberField--ltr']/div[@class='CardNumberField-input-wrapper']/input").send_keys("4545 4545 4545 4545")
driverChrome.switch_to.default_content()
driverChrome.switch_to.frame("__privateStripeFrame83643")
driverChrome.find_element(By.NAME, value="cvc").send_keys("254")
time.sleep(5)

print("Test Passed")