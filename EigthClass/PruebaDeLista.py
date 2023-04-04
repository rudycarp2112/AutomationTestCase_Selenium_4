import random
import string
import time
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

# servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
# driverChrome=webdriver.Chrome(service=servObj)
# driverChrome.implicitly_wait(10)
#
# driverChrome.get("https://admin-demo.nopcommerce.com/login") # Play with de UI elements
# driverChrome.maximize_window()
# chrome=Chrome()
# chrome.get("https://admin-demo.nopcommerce.com/login")
# time.sleep(3)

# driverChrome.switch_to.frame(0)
# driverChrome.find_element(By.XPATH,"//input[@type='checkbox']").click()
# driverChrome.switch_to.default_content()

def ClickOnCustomerRole(driver):
    div_customerRole=driver.find_element(By.XPATH,"//div[@class='input-group-append input-group-required']//div[@class='k-widget k-multiselect k-multiselect-clearable']").click()

# def random_generator_char(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
#
# name=random_generator_char() + "@gmail.com"
# print(name)

msg = "Victoria Mercedes"
x=msg.split()
print(x[0])

# txt_username_id="Email"
# txt_pass_id="Password"
# btn_login_xpath="//button[normalize-space()='Log in']"
# btn_logout_linktext="Logout"
#
# btn_customersMenu_lknText="Customers"
# btn_optionCustomers_xpath="//a[@href='/Admin/Customer/List']"
# btn_addCustomer_xpath="//a[normalize-space()='Add new']"
#
# chrome.find_element(By.ID,txt_username_id).clear()
# chrome.find_element(By.ID,txt_username_id).send_keys("admin@yourstore.com")
# chrome.find_element(By.ID,txt_pass_id).clear()
# chrome.find_element(By.ID,txt_pass_id).send_keys("admin")
# chrome.find_element(By.XPATH,btn_login_xpath).click()
#
# chrome.find_element(By.LINK_TEXT,btn_customersMenu_lknText).click()
# chrome.find_element(By.XPATH,btn_optionCustomers_xpath).click()
# chrome.find_element(By.XPATH,btn_addCustomer_xpath).click()
#
# ##### Probar seleccionador de roles
# div_customerRole_xpath = "(//div[@role='listbox'])[2]"
# ddl_customerRole_xpath = "//select[@id='SelectedCustomerRoleIds']"
# list_selectCustomerRole_xpath= "//ul[@id='SelectedCustomerRoleIds_taglist']//li"
# role="Guests"
#
# lst_customerRoleSelected=chrome.find_elements(By.XPATH,list_selectCustomerRole_xpath)
# ddl_customerRole=chrome.find_element(By.XPATH,ddl_customerRole_xpath)
# ddl_customerRoleOptions=Select(ddl_customerRole)
#
# if role == "Guests":
#     for row in range(0, len(lst_customerRoleSelected)):
#         if lst_customerRoleSelected[row].text == "Registered":
#             chrome.find_element(By.XPATH, div_customerRole_xpath).click()
#             chrome.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Registered']").click()
#             break
#     chrome.find_element(By.XPATH, div_customerRole_xpath).click()
#     chrome.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='"+role+"']").click()
#
# elif role == "Administrators":
#     chrome.find_element(By.XPATH, div_customerRole_xpath).click()
#     chrome.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Forum Moderators']").click()
#     # optAdministrator=driverChrome.find_element(By.XPATH,"//li[contains(text(),'Administrators')]")
#     # driverChrome.execute_script("arguments[0].click()",optAdministrator)
#     time.sleep(5)
#     # driverChrome.find_element(By.XPATH, "//select[@id='SelectedCustomerRoleIds']//option[normalize-space()='Administrators']").click()
#     # ddl_customerRoleOptions.select_by_visible_text(role)
# elif role == "Forum Moderators":
#     ClickOnCustomerRole(chrome)
#     ddl_customerRoleOptions.select_by_visible_text(role)
# elif role == "Vendors":
#     ClickOnCustomerRole(chrome)
#     ddl_customerRoleOptions.select_by_visible_text(role)
# else:
#     for row in range(1, len(lst_customerRoleSelected) + 1):
#         if lst_customerRoleSelected[row].text == "Guests":
#             ClickOnCustomerRole(chrome)
#             ddl_customerRoleOptions.select_by_visible_text("Guests")  # delete Registered initial option
#             break
#         ClickOnCustomerRole(chrome)
#         ddl_customerRoleOptions.select_by_visible_text(role)
#
# time.sleep(5)
# chrome.close()