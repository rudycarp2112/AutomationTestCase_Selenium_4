import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Select
import mysql


# Once you have been installed MySQL DB, only there you should continue with this final class...
# As automate tester we only use the next sentences on the database: DML and DRL (sub languages from SQL) in MySQL WorkBench (client GUI of MySQL Server)

# As DB tester we need to perform aditional actions on DB such as read intern registers the some tables and how they have been inserted once the APP send the data

#1 Install this connector: mysql-connector-python (package)
#2 DB operations: insert,update,detele,select
def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

querySelect="select * from calcdata"
driverC=chrome_setup()
driverC.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driverC.maximize_window()

time.sleep(5)
driverC.find_element(By.ID,"wzrk-cancel").click()
try:
    con= mysql.connector.connect(host="localhost", port="3306", user="Rudy2", passwd="zinc23_._ARG", database="world")
    curs=con.cursor()
    curs.execute(querySelect) #we can execute other type of commands too

    for row in curs:
        price=row[0]
        rateOfInterest =row[1]
        periodNum =row[2]
        periodName =row[3]
        frecuency =row[4]
        maturityValueExpected =row[5]

        # Passing data to the application
        driverC.find_element(By.XPATH, "//input[@id='principal']").send_keys(price)
        driverC.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateOfInterest)
        driverC.find_element(By.XPATH, "//input[@id='tenure']").send_keys(periodNum)
        ddlPeriod=driverC.find_element(By.XPATH, "//select[@id='tenurePeriod']")
        ddlPeriodOptions=Select(ddlPeriod)
        ddlPeriodOptions.select_by_visible_text(periodName)

        ddlFrecuency=driverC.find_element(By.XPATH, "//select[@id='frequency']")
        ddlFrecuencyOptions=Select(ddlFrecuency)
        ddlFrecuencyOptions.select_by_visible_text(frecuency)

        driverC.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click() #Calculate button

        result=driverC.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
        #Validate
        if float(maturityValueExpected)==float(result): #Or instead of parse them to string, we can parse to float()
            print("Test Passed")
        else:
            print("Test Failed")

        driverC.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # Clear button

    con.close()

except:
    print("Connection unsuccesfull...")

driverC.close()