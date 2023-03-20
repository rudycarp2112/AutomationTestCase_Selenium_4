
from selenium import webdriver
from selenium import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\Pycharm2023\webdriver\chromedriver")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/?stype=lo&jlou=AferocbhzszZvg2vBBqOrtMADeS5i8TnGZ-vroGnpxQA7KGTqisku1isClsR38QzMmIDW_XHH6rBKBs4TnG5ApOQLM5FQHCaCkILoDyW8N-_wQ&smuh=37133&lh=Ac9NrOU87PHG1MvV1Oc")

# tag and name combination -> sintax: tagname#nameValue
# driver.find_element(By.CSS_SELECTOR, value="#email").send_keys("franco.rudy@hotmail.com")
# driver.find_element(By.CSS_SELECTOR, value="input#email").send_keys("franco.rudy@hotmail.com")

# tag and class combination -> sintax: tagname.classValue
# driver.find_element(By.CSS_SELECTOR, value=".inputtext").send_keys("franco.rudy@hotmail.com") #without TAG
# driver.find_element(By.CSS_SELECTOR, value="input.inputtext").send_keys("franco.rudy@hotmail.com")

# tag and attribute combination -> sintax: tagname[attribute=attributeValue]
# driver.find_element(By.CSS_SELECTOR, value="input[data-testid=royal_email]").send_keys("franco.rudy@hotmail.com")
# driver.find_element(By.CSS_SELECTOR, value="[data-testid=royal_email]").send_keys("franco.rudy@hotmail.com")

# tag, class and attribute combination -> sintax: tagname.classValue[attribute=attributeValue]
driver.find_element(By.CSS_SELECTOR, value="input.inputtext[data-testid=royal_email]").send_keys("franco.rudy@hotmail.com")
driver.find_element(By.CSS_SELECTOR, value="input.inputtext[data-testid=royal_pass]").send_keys("1234569")