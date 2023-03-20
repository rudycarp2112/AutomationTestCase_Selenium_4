from NopCommerceApp_Hybrid_FW.pageObjects.LoginPage import LoginPage


# https://youtu.be/57pjD89IFXA?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&t=4435
class Test_001_Login:
    base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_homePageTittle(self, setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.act_tittle=self.driver.title

        if self.act_tittle=="Your store. Login123":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_homePageTittle.png")
            self.driver.close()
            assert False
    def test_login(self, setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.loginP= LoginPage(self.driver)
        self.loginP.setUserName(self.username)
        self.loginP.setPassword(self.password)
        self.loginP.login()
        act_tittle=self.driver.title

        if act_tittle=="Dashboard / nopCommerce administration123":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False


