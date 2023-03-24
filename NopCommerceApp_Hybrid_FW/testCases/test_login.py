from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig #To access to config.ini file data
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration

# https://youtu.be/y2Kz3QaZcVo?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&t=2888
class Test_001_Login:
    base_url=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()

    logger=LogGeneration.Loggen()

    def test_homePageTittle(self, setup):
        self.logger.info("**************************** Test_001_Login ****************************")
        self.logger.info("**************************** Verifying Home Page Title ****************************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.act_tittle=self.driver.title

        if self.act_tittle=="Your store. Login":
            self.driver.close()
            self.logger.info("**************************** Verifying Home Page Title: Passed ****************************")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_homePageTittle.png")
            self.driver.close()
            self.logger.error("**************************** Verifying Home Page Title: Failed ****************************")
            assert False
    def test_login(self, setup):
        self.logger.info("**************************** Test_001_Login ****************************")
        self.logger.info("**************************** Verifying Login Home Page ****************************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.loginP= LoginPage(self.driver)
        self.loginP.setUserName(self.username)
        self.loginP.setPassword(self.password)
        self.loginP.login()
        act_tittle=self.driver.title

        if act_tittle=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("**************************** Verifying Login Home Page: Passed ****************************")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**************************** Verifying Login Home Page: Failed ****************************")
            assert False


