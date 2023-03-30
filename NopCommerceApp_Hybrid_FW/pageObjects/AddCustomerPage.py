import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class AddCustomer():

    # Identify WebElement writing their locators
    btn_customersMenu_lknText="Customers"
    btn_optionCustomers_xpath="//a[@href='/Admin/Customer/List']"
    btn_addCustomer_xpath="//a[normalize-space()='Add new']"

    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstName_id = "FirstName"
    txt_lastName_id = "LastName"
    rdBtn_genderMale_id = "Gender_Male"
    rdBtn_genderFemale_id = "Gender_Female"
    txt_dateOfBirth_id = "DateOfBirth"
    txt_companyName_id = "Company"
    ckb_isTaxExempt_id = "IsTaxExempt"

    div_newsLetter_xpath = "(//div[@role='listbox'])[1]"
    # lst_selectedNewsLetter_xpath = "(//div[@role='listbox'])[1]"
    opt_yourStoreName_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']//li[contains(text(),'Your store name')]"
    opt_TestStore2_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']//li[contains(text(),'Test store 2')]"
    # ddl_newsLetter_id="SelectedNewsletterSubscriptionStoreIds"

    #//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[2]//span
    div_customerRole_xpath = "(//div[@role='listbox'])[2]" # Click to show the options of DropDownList
    lst_selectedCustomerRoles_id = "//ul[@id='SelectedCustomerRoleIds_taglist']//li"  # List of role tags selected
    opt_roleForumModerators_xpath="//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Forum Moderators']"
    opt_roleAdministrators_xpath ="//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Administrators']"
    opt_roleGuests_xpath ="//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Guests']"
    opt_roleRegistered_xpath ="//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Registered']"
    opt_roleVendors_xpath ="//ul[@id='SelectedCustomerRoleIds_listbox']//li[normalize-space()='Vendors']"

    # deleteBtn_selectCustomerRole_xpath="//span[@class='k-icon k-i-close']" # another option: //ul[@id='SelectedCustomerRoleIds_taglist']/li[2]//span[@class='k-icon k-i-close']
    ddl_manageOfVendor_id="VendorId"
    ckb_active_id="Active"
    txt_adminContent_id="AdminComment"
    btn_save_name="save"

    def __init__(self, driver):
        self.driver=driver
        # Create WebElements objects
        # self.ddl_newsLetterOptions = Select(self.ddl_newsLetter)
        # self.ddl_customerRole = self.driver.find_element(By.ID,self.ddl_customerRole_xpath)
        # self.ddl_customerRoleOptions = Select(self.ddl_customerRole)
        # self.list_selectCustomerRole = self.driver.find_element(By.ID,self.list_selectCustomerRole_id)
        # self.deleteBtn_selectCustomerRole = self.driver.find_element(By.XPATH,self.deleteBtn_selectCustomerRole_xpath)

    def clickOnCustomerMenu(self):
        self.btn_customersMenu = self.driver.find_element(By.LINK_TEXT, self.btn_customersMenu_lknText)
        self.btn_customersMenu.click()

    def clickOnOptionCustomer(self):
        self.btn_optionCustomers = self.driver.find_element(By.XPATH, self.btn_optionCustomers_xpath)
        self.btn_optionCustomers.click()

    def clickOnAddCustomer(self):
        self.btn_addCustomer = self.driver.find_element(By.XPATH, self.btn_addCustomer_xpath)
        self.btn_addCustomer.click()

    def clickOnSave(self):
        self.btn_save = self.driver.find_element(By.NAME, self.btn_save_name)
        self.btn_save.click()

    def setEmail(self,Email):
        self.txt_email = self.driver.find_element(By.ID, self.txt_email_id)
        self.txt_email.clear()
        self.txt_email.send_keys(Email)

    def setPassword(self,Pass):
        self.txt_password = self.driver.find_element(By.ID, self.txt_password_id)
        self.txt_password.clear()
        self.txt_password.send_keys(Pass)
    def setFirstName(self,Name):
        self.txt_firstName = self.driver.find_element(By.ID, self.txt_firstName_id)
        self.txt_firstName.clear()
        self.txt_firstName.send_keys(Name)
    def setLastName(self,LastName):
        self.txt_lastName = self.driver.find_element(By.ID, self.txt_lastName_id)
        self.txt_lastName.clear()
        self.txt_lastName.send_keys(LastName)
    def setGenderMale(self):
        self.rdBtn_genderMale = self.driver.find_element(By.ID, self.rdBtn_genderMale_id)
        self.rdBtn_genderMale.click()

    def setGenderFemale(self):
        self.rdBtn_genderFemale = self.driver.find_element(By.ID, self.rdBtn_genderFemale_id)
        self.rdBtn_genderFemale.click()
    def setBirth(self, date):
        self.txt_dateOfBirth = self.driver.find_element(By.ID, self.txt_dateOfBirth_id)
        self.txt_dateOfBirth.clear()
        self.txt_dateOfBirth.send_keys(date)
    def setCompanyName(self,Company):
        self.txt_companyName = self.driver.find_element(By.ID, self.txt_companyName_id)
        self.txt_companyName.clear()
        self.txt_companyName.send_keys(Company)
    def setTaxExempt(self):
        self.ckb_isTaxExempt = self.driver.find_element(By.ID, self.ckb_isTaxExempt_id)
        self.ckb_isTaxExempt.click()

    def setManageVendor(self, numOfVendor):
        # Make it to verify if the customer has the role "Vendor"
        self.ddl_manageOfVendor = self.driver.find_element(By.ID, self.ddl_manageOfVendor_id)
        self.ddl_manageOfVendorOptions = Select(self.ddl_manageOfVendor)
        self.ddl_manageOfVendorOptions.select_by_visible_text(numOfVendor)

    def setActive(self):
        self.ckb_active = self.driver.find_element(By.ID, self.ckb_active_id)
        self.ckb_active.click()

    def setAdminComment(self, comment):
        self.txt_adminContent = self.driver.find_element(By.ID, self.txt_adminContent_id)
        self.txt_adminContent.clear()
        self.txt_adminContent.send_keys(comment)

    def setNewsLetter(self,option):
        self.div_newsLetter = self.driver.find_element(By.XPATH, self.div_newsLetter_xpath)
        self.opt_newsYourStore = self.driver.find_element(By.XPATH, self.opt_yourStoreName_xpath)
        self.opt_newsTestStore = self.driver.find_element(By.XPATH, self.opt_TestStore2_xpath)
        self.div_newsLetter.click()
        # self.list_newsLetter = self.driver.find_element(By.XPATH, self.lst_selectedNewsLetter_xpath)
        if option=="Your store name":
            self.opt_newsYourStore.click()
        else:
            self.opt_newsTestStore.click()
    def ClickOnCustomerRole(self):
        self.div_customerRole = self.driver.find_element(By.XPATH, self.div_customerRole_xpath)
        self.div_customerRole.click()
        time.sleep(2)
    def setCustomerRole(self,role):
        self.opt_roleForumModerators = self.driver.find_element(By.XPATH, self.opt_roleForumModerators_xpath)
        self.opt_roleAdministrators = self.driver.find_element(By.XPATH, self.opt_roleAdministrators_xpath)
        self.opt_roleGuests = self.driver.find_element(By.XPATH, self.opt_roleGuests_xpath)
        self.opt_roleRegistered = self.driver.find_element(By.XPATH, self.opt_roleRegistered_xpath)
        self.opt_roleVendors = self.driver.find_element(By.XPATH, self.opt_roleVendors_xpath)
        self.list_customerRoleSelected = self.driver.find_elements(By.XPATH, self.lst_selectedCustomerRoles_id)

        if role == "Guests":
            for row in range(0,len(self.list_customerRoleSelected)):
                if self.list_customerRoleSelected[row].text == "Registered":
                    self.ClickOnCustomerRole()
                    self.opt_roleRegistered.click()
                    break
            self.ClickOnCustomerRole()
            self.opt_roleGuests.click()
        elif role == "Administrators":
            self.ClickOnCustomerRole()
            self.opt_roleAdministrators.click()
        elif role == "Forum Moderators":
            self.ClickOnCustomerRole()
            self.opt_roleForumModerators.click()
        elif role == "Vendors":
            self.ClickOnCustomerRole()
            self.opt_roleVendors.click()
        else:
            for row in range(0, len(self.list_customerRoleSelected)):
                if self.list_customerRoleSelected[row].text == "Guests":
                    self.ClickOnCustomerRole()
                    self.opt_roleGuests.click()
                    break
            self.ClickOnCustomerRole()
            self.opt_roleRegistered.click()




