# In a real time proyect we usually write TDD which are contain some basic operations such as:
# - Read/Writen excel
# - Apply colors to cells
# - count rows and columns
# - Automation Code

# automation code + excel operations code = complex. Generally, the excel operations will be reapeat for every TC for this reason we need create functions
# are which allow us use the same operaions. This can realize with a module that contains these functions: read(),writing(),color(), etc.
# This file receive the name of Utility File
# This manner we always have TC with automation code and validations only, whitout repeat excel operation. We avoid writing one more time the excel operations.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Select
from FourteenthClass import XLUtils


# Its recommend whenever some TC fail we capture the error and serve as envidence for the developer
def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

file="C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\FourteenthClass\\CalculatorData.xltx"
sheet="Hoja1"
numRows=XLUtils.getRowCount(file,sheet)
numCols=XLUtils.getColumnCount(file,sheet)

driverC=chrome_setup()
driverC.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driverC.maximize_window()

time.sleep(8)
driverC.find_element(By.ID,"wzrk-cancel").click()

for r in range(2,numRows+1):

    price=XLUtils.readData(file,sheet,r,1)
    rateOfInterest = XLUtils.readData(file, sheet, r, 2)
    periodNum = XLUtils.readData(file, sheet, r, 3)
    periodName = XLUtils.readData(file, sheet, r, 4)
    frecuency = XLUtils.readData(file, sheet, r, 5)
    maturityValueExpected = XLUtils.readData(file, sheet, r, 6)

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
        XLUtils.fillGreen(file, sheet, r, 8)
        XLUtils.writeData(file,sheet,r,8,"Pass")
    else:
        print("Test Failed")
        XLUtils.fillRed(file, sheet, r, 8)
        XLUtils.writeData(file, sheet, r, 8, "Fail")

    driverC.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # Clear button

driverC.close()