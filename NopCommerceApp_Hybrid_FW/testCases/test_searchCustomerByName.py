import time

import pytest

from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.pageObjects.AddCustomerPage import AddCustomer
from NopCommerceApp_Hybrid_FW.pageObjects.SearchCustomerPage import SearchCustomer
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig

class Test_005_searchCustomerByName:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGeneration.Loggen()
    nameToSearch = "Victoria"

    @pytest.mark.regression
    def test_searchCustomerByCorrectName(self, setup):
        LogGeneration.msgInfoLogFile(self.logger, "Test_005_searchCustomerByName")
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
        self.sc.setName(self.nameToSearch)
        self.sc.clickOnSearch()
        LogGeneration.msgInfoLogFile(self.logger, "Search Finished")

        LogGeneration.msgInfoLogFile(self.logger, "Verifying Search")
        result=self.sc.validateSearchForFirstName(self.nameToSearch)

        if result==True:
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Search: OK")
            LogGeneration.msgInfoLogFile(self.logger, "TC_searchCustomerByCorrectName: Passed")
            assert result
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_searchCustomerByCorrectEmail.png")
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Search: NOT OK")
            LogGeneration.msgInfoLogFile(self.logger, "TC_searchCustomerByCorrectName: Failed")
            assert result
        self.driver.close()

