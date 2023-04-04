import pytest

from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig #To access to config.ini file data
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration

class Test_001_Login:
    base_url=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()

    logger=LogGeneration.Loggen()

    @pytest.mark.regression
    def test_homePageTittle(self, setup):
        self.driver = setup
        LogGeneration.msgInfoLogFile(self.logger, "Test_001_Login")
        LogGeneration.msgInfoLogFile(self.logger, "Verifying Home Page Title")
        self.driver.get(self.base_url)
        self.act_tittle=self.driver.title

        if self.act_tittle=="Your store. Login":
            self.driver.close()
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Home Page Title: Passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_homePageTittle.png")
            self.driver.close()
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Home Page Title: Failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        LogGeneration.msgInfoLogFile(self.logger, "Test_001_Login")
        LogGeneration.msgInfoLogFile(self.logger, "Verifying Login Home Page")
        self.driver=setup
        self.driver.get(self.base_url)
        self.loginP= LoginPage(self.driver)
        self.loginP.setUserName(self.username)
        self.loginP.setPassword(self.password)
        self.loginP.login()
        act_tittle=self.driver.title

        if act_tittle=="Dashboard / nopCommerce administration":
            self.driver.close()
            LogGeneration.msgInfoLogFile(self.logger, "Verifying Login Home Page: Passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_login.png")
            self.driver.close()
            LogGeneration.msgErrorLogFile(self.logger, "Verifying Login Home Page: Failed")
            assert False


