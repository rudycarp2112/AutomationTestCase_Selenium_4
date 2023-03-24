from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig #To access to config.ini file data
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration
from NopCommerceApp_Hybrid_FW.utilities import XLUtils

# https://youtu.be/y2Kz3QaZcVo?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&t=2888
class Test_002_DDT_Login:
    base_url=ReadConfig.getApplicationUrl()
    pathLoginData="C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\TestData\\LoginData.xlsx"
    logger=LogGeneration.Loggen()
    numRow = XLUtils.getRowCount(pathLoginData, "Sheet1")
    numCols= XLUtils.getColumnCount(pathLoginData, "Sheet1")

    def test_login_ddt(self, setup):
        self.logger.info("**************************** Test_002_DDT_Login ****************************")
        self.logger.info("**************************** Verifying Login DDT Home Page ****************************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.loginP= LoginPage(self.driver)
        self.lst_status=[]

        for row in range(2, self.numRow+1):
            self.username=XLUtils.readData(self.pathLoginData,"Sheet1",row,1)
            self.password=XLUtils.readData(self.pathLoginData,"Sheet1",row,2)
            self.expected = XLUtils.readData(self.pathLoginData, "Sheet1",row,3)

            self.loginP.setUserName(self.username)
            self.loginP.setPassword(self.password)
            self.loginP.login()
            act_tittle=self.driver.title
            exp_tittle="Dashboard / nopCommerce administration"

            if act_tittle==exp_tittle:
                if self.expected=="Pass":
                    self.logger.info("**************************** Passed ****************************")
                    self.lst_status.append("Pass")
                    self.loginP.logout()
                    assert True
                else:
                    self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_login_" + str(row) + ".png")
                    self.logger.error("**************************** Failed ****************************")
                    self.lst_status.append("Fail")
                    self.loginP.logout()
                    assert False
            else:
                if self.expected=="Pass":
                    self.logger.error("**************************** Failed ****************************")
                    self.lst_status.append("Fail")
                    assert False
                else:
                    self.lst_status.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_login_" + str(row) + ".png")
                    self.logger.info("**************************** Passed ****************************")
                    assert True

        if "Fail" not in self.lst_status:
            self.logger.info("***** Login DDT Passed *****")
        else:
            self.logger.info("***** Login DDT Failed *****")

        self.logger.info("****** END of Login DDT ******")
        self.logger.info("****** Completed Test_002_DDT_Login ******")

        self.driver.close()

