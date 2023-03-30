import random
import string
import time

from selenium.webdriver.common.by import By
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration
from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.pageObjects.AddCustomerPage import AddCustomer
# https://youtu.be/nsjQigkkpVY?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&t=3154

def random_generator_char(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    usermail = ReadConfig.getUserEmail()
    userpwd = ReadConfig.getUserPassword()
    logger = LogGeneration.Loggen()

    def test_addCustomer(self,setup):
        self.logger.info("************ Test_003_AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(2)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usermail)
        self.lp.setPassword(self.userpwd)
        self.lp.login()
        self.logger.info("************ Loggin Succesful ************")

        self.logger.info("************ Test_003_AddCustomer ************")
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomerMenu()
        self.ac.clickOnOptionCustomer()
        self.ac.clickOnAddCustomer()

        self.logger.info("************ screen location 'Add customer' Succesful ************")
        self.logger.info("************ Starting Add Customer ***********")

        self.email = random_generator_char() + "@gmail.com"
        self.ac.setEmail(self.email)
        self.ac.setPassword("test123")
        self.ac.setFirstName("Franco")
        self.ac.setLastName("Rudy")
        self.ac.setGenderMale()
        self.ac.setBirth("9/16/1998")
        self.ac.setCompanyName("Utest")
        self.ac.setNewsLetter("Test store 2")
        self.ac.setCustomerRole("Administrators")
        time.sleep(1)
        self.ac.setCustomerRole("Forum Moderators")
        self.ac.setAdminComment("Test User was created for test purpose")

        self.ac.clickOnSave()

        self.logger.info("************ Saving Customer info ***********")
        self.logger.info("************ Add Customer validation started ***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*************** Add customer test Passed ***************")
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"add_customer_src.png")
            self.logger.info("*************** Add customer test Failed ***************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending Test_003_AddCustomer TC ***************")








