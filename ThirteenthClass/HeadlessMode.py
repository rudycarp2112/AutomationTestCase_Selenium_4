from selenium import webdriver


#Advantage
# - the script only execute in the backend whithout display the browser with ui elements
# - is faster so consume minu time (the performance will be increase)
#disadvantage (some times is very useful)
# - once its executed the program we cant perform any action
# - we cant see if the browser is doing actions correctly

# The headless mode will be execute different for every browser
def headless_chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    options= webdriver.ChromeOptions()
    options.add_argument("--headless")
    driverChrome = webdriver.Chrome(service=servObj, options=options) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

def headless_edge_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\msedgedriver")
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driverEdge = webdriver.Edge(service=servObj, options=options)
    driverEdge.implicitly_wait(10)

    return driverEdge

def headless_firefox_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # necessary to locate firefox .exe
    options.add_argument("--headless")
    driverFirefox = webdriver.Firefox(service=servObj, options=options)
    driverFirefox.implicitly_wait(10)

    return driverFirefox

# driverC=headless_chrome_setup()
# driverE=headless_edge_setup()
driverF=headless_firefox_setup()

# driverC.get("https://demo.nopcommerce.com")
# print(driverC.title)
# print(driverC.current_url)
# driverC.close()

# driverE.get("https://demo.nopcommerce.com")
# print(driverE.title)
# print(driverE.current_url)
# driverE.close()

driverF.get("https://demo.nopcommerce.com")
print(driverF.title)
print(driverF.current_url)
driverF.close()