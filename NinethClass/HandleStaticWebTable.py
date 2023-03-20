# https://youtu.be/GU_rBth5QpI?list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&t=3597
# 1) Count number of rows and columns
# 2) Read specific row and column data
# 3) Read all the rows and columns data
# 4) Read data based oin condition (List books name whose the autor is Mukesh)

from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

servObj=Service("C:\Pycharm2023\webdriver\chromedriver")
driverChrome= webdriver.Chrome(service=servObj)
driverChrome.implicitly_wait(10)

driverChrome.get("https://testautomationpractice.blogspot.com")
driverChrome.maximize_window()

numOfRows=len(driverChrome.find_elements(By.XPATH, value="//table[@name='BookTable']//tr")) # include header
numOfCols=len(driverChrome.find_elements(By.XPATH, value="//table[@name='BookTable']//tr/th")) # same result= //table[@name='BookTable']//tr[1]/th

print("Number of rows: " + str(numOfRows) + " - " + "Number of columns: " + str(numOfCols))

# 2) Read specific row and column data - value: JAVA
value=driverChrome.find_element(By.XPATH, value="//table[@name='BookTable']//tr[6]/td[3]")

print("Value obtained: " + value.text)

# 3) Read all the rows and columns data
# for r in range(2, numOfRows+1):
#     print("\nRow number: " + str(r-1))
#     for c in range(1, numOfCols+1):
#         textData=driverChrome.find_element(By.XPATH, value="//table[@name='BookTable']//tr["+ str(r) +"]/td["+ str(c) +"]")
#         print(textData.text, end="    ")

# 4) Read data based oin condition (List books name whose the autor is Mukesh)
for r in range(2, numOfRows+1):
    nameAuthor=driverChrome.find_element(By.XPATH, value="//table[@name='BookTable']//tr["+ str(r) +"]/td[2]").text
    if nameAuthor=="Mukesh":
        bookName=driverChrome.find_element(By.XPATH, value="//table[@name='BookTable']//tr["+ str(r) +"]/td[1]").text
        print("Book Name: " + bookName + " - Author: " + nameAuthor)

driverChrome.close()