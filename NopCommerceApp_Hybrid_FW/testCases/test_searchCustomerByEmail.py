import time

from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.pageObjects.AddCustomerPage import AddCustomer
from NopCommerceApp_Hybrid_FW.pageObjects.SearchCustomerPage import SearchCustomer
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig

class Test_004_searchCustomerByEmail:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGeneration.Loggen()
    emailToValidate = "brenda_lindgren@nopCommerce.com"

    def test_searchCustomerByCorrectEmail(self, setup):
        LogGeneration.msgInfoLogFile(self.logger, "Test_004_searchCustomerByEmail")
        self.driver = setup
        self.driver.get(self.base_url)

        LogGeneration.msgInfoLogFile(self.logger, "Login Page")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        LogGeneration.msgInfoLogFile(self.logger, "Login Page Successful")

        LogGeneration.msgInfoLogFile(self.logger, "Moving to Search Customer Screen")
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomerMenu()
        self.ac.clickOnOptionCustomer()
        LogGeneration.msgInfoLogFile(self.logger, "Into Search Customer Screen")

        LogGeneration.msgInfoLogFile(self.logger, "Start Search")
        self.sc = SearchCustomer(self.driver)
        self.sc.setEmail(self.emailToValidate)
        self.sc.clickOnSearch()
        LogGeneration.msgInfoLogFile(self.logger, "Search Finished")

        LogGeneration.msgInfoLogFile(self.logger, "Verifying Search")
        result=self.sc.validateSearchForEmail(self.emailToValidate)

        if result==True:
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Search: OK")
            LogGeneration.msgInfoLogFile(self.logger, "TC_searchCustomerByCorrectEmail: Passed")
            assert result
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_searchCustomerByCorrectEmail.png")
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Search: NOT OK")
            LogGeneration.msgInfoLogFile(self.logger, "TC_searchCustomerByCorrectEmail: Failed")
            assert result
        self.driver.close()

