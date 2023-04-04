import pytest

from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage
from NopCommerceApp_Hybrid_FW.utilities.readProperties import ReadConfig #To access to config.ini file data
from NopCommerceApp_Hybrid_FW.utilities.customLogger import LogGeneration
from NopCommerceApp_Hybrid_FW.utilities import XLUtils

class Test_002_DDT_Login:
    base_url=ReadConfig.getApplicationUrl()
    pathLoginData="C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\TestData\\LoginData.xlsx"
    logger=LogGeneration.Loggen()
    numRow = XLUtils.getRowCount(pathLoginData, "Sheet1")
    numCols= XLUtils.getColumnCount(pathLoginData, "Sheet1")

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        LogGeneration.msgInfoLogFile(self.logger, "Test_002_DDT_Login")
        LogGeneration.msgInfoLogFile(self.logger, "Verifying Login DDT Home Page")
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
                    LogGeneration.msgInfoLogFile(self.logger, "Passed")
                    self.lst_status.append("Pass")
                    self.loginP.logout()
                    assert True
                else:
                    self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_login_" + str(row) + ".png")
                    LogGeneration.msgErrorLogFile(self.logger, "Failed")
                    self.lst_status.append("Fail")
                    self.loginP.logout()
                    assert False
            else:
                if self.expected=="Pass":
                    LogGeneration.msgErrorLogFile(self.logger, "Failed")
                    self.lst_status.append("Fail")
                    assert False
                else:
                    self.lst_status.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + "test_login_" + str(row) + ".png")
                    LogGeneration.msgInfoLogFile(self.logger, "Passed")
                    assert True

        if "Fail" not in self.lst_status:
            LogGeneration.msgInfoLogFile(self.logger, "Login DDT Passed")
        else:
            LogGeneration.msgInfoLogFile(self.logger, "Login DDT Failed")

        LogGeneration.msgInfoLogFile(self.logger, "END of Login DDT")
        LogGeneration.msgInfoLogFile(self.logger, "Completed Test_002_DDT_Login")

        self.driver.close()

