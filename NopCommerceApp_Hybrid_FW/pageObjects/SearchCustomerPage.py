from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomer():
    # For search a customer
    txt_emailCustomer_id = "SearchEmail"
    txt_firstNameCustomer_id = "SearchFirstName"
    txt_lastNameCustomer_id = "SearchLastName"
    ddl_monthBirth_id = "SearchMonthOfBirth"
    ddl_dayBirth_id = "SearchDayOfBirth"
    txt_registrationDateFrom_id = "SearchRegistrationDateFrom"
    txt_registrationDateTo_id = "SearchRegistrationDateTo"
    txt_lastActivityFrom_id = "SearchLastActivityFrom"
    txt_lastActivityTo_id = "SearchLastActivityTo"
    txt_company_id = "SearchCompany"
    txt_ipAddress_id = "SearchIpAddress"

    div_customerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"

    btn_search_id = "search-customers"

    table_SearchCustomer_id = "customers-grid"
    table_SearchCustomerRows_xpath = "//table[@id='customers-grid']//tbody//tr"
    table_SearchCustomerCols_xpath = "//table[@id='customers-grid']//tbody//tr[1]//td"

    def __init__(self, driver):
        self.driver=driver

    def setEmail(self,email):
        txt_email=self.driver.find_element(By.ID,self.txt_emailCustomer_id)
        txt_email.clear()
        txt_email.send_keys(email)
    def setName(self, name):
        txt_name=self.driver.find_element(By.ID,self.txt_firstNameCustomer_id)
        txt_name.clear()
        txt_name.send_keys(name)

    def setLastName(self, lastName):
        txt_lastName=self.driver.find_element(By.ID,self.txt_lastNameCustomer_id).clear()
        txt_lastName.send_keys(lastName)

    def clickOnSearch(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def numberOfRows(self):
        rows = self.driver.find_elements(By.XPATH,self.table_SearchCustomerRows_xpath)
        return len(rows)
    def numberOfCols(self):
        cols = self.driver.find_elements(By.XPATH,self.table_SearchCustomerCols_xpath)
        return len(cols)

    def validateSearchForEmail(self, email):
        numRows = self.numberOfRows()
        for row in range(1,numRows+1):
            valueEmail=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(row)+"]//td[2]").text
            if email == valueEmail:
                return True
        return False

    def validateSearchForFirstName(self, name):
        numRows = self.numberOfRows()
        for row in range(1,numRows+1):
            valueFirstName=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody//tr["+str(row)+"]//td[3]").text
            arrayName = valueFirstName.split()
            if name in arrayName[0]:
                return True
        return False