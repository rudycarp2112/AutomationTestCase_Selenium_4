import time
from selenium import webdriver


# Its recommend whenever some TC fail we capture the error and serve as envidence for the developer
def chrome_setup():
    from selenium import Service
    servObj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driverChrome = webdriver.Chrome(service=servObj) #This way we pass where is the path that we want receive the download file
    driverChrome.implicitly_wait(10)

    return driverChrome

driverC=chrome_setup()
driverC.get("https://demo.nopcommerce.com")
driverC.maximize_window()

# driverC.save_screenshot("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\ThirteenthClass\\homepage.png")
time.sleep(2) # to make it appear sharper
# driverC.save_screenshot(os.getcwd()+"\\homepage.png")
# driverC.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

#Methods that capture screenshot and returns it as binary format (ASCII code)
# driverC.get_screenshot_as_png()
# driverC.get_screenshot_as_base64()

driverC.close()