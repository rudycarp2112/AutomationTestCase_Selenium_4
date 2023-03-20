# We need identify those webElements locators to work in login web page
# Data of login: mail-rudyxptrent@hotmail.com and pws-admin123

from selenium.webdriver.common.by import By


class LoginPage:
    txt_username_id="Email"
    txt_pass_id="Password"
    btn_login_xpath="//button[normalize-space()='Log in']"
    btn_logout_linktext="Logout"

    #we need create a constructor for realize actions in each locator

    # This function as a constructor will be initialize automatically when the class is called
    def __init__(self, driver):
        self.driver=driver # Now this class its will be initialize with a variable call driver which will be called in other functions of this class

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.txt_username_id).clear()
        self.driver.find_element(By.ID,self.txt_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txt_pass_id).clear()
        self.driver.find_element(By.ID,self.txt_pass_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_logout_linktext).click()