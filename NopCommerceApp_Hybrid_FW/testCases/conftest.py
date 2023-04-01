from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        serv_obj = Service("C:\\Pycharm2023\\webdriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == "chromeWithSecureCaptcha":
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == "firefox":
        serv_obj = Service("C:\\Pycharm2023\\webdriver\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # necessary to locate firefox .exe
        driver = webdriver.Firefox(service=serv_obj, options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
    else:
        serv_obj = Service("C:\\Pycharm2023\\webdriver\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
        driver.implicitly_wait(10)
        driver.maximize_window()

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hook
    # parser.addoption("--browser")
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox or edge"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption(
        "--browser")  # pytest -v -s NopCommerceApp_Hybrid_FW/testCases/test_login.py --browser chrome


############# To Generato HTML reports
# Its hook for Adding Environment info to HTML Reports
def pytest_configure(config):
    config._metadata["Proyect Name"] = "Nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Franco Rudy"


# It is hook for Delete/Modify Environment info to HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # For default, the HTML Reports add this info, so we no need for this case.
    metadata.pop("Plugins", None)
