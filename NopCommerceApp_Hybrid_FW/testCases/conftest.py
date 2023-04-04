from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup(browser):
    global driver
    if browser == "chrome":
        serv_obj = Service("C:\\Pycharm2023\\webdriver\\chromedriver.exe")
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
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
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox or edge"
    )


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")  # pytest -v NopCommerceApp_Hybrid_FW/testCases/test_login.py --browser chrome


############# To Generate HTML reports
# Its hook for Adding Environment info to HTML Reports
def pytest_configure(config):
    config._metadata["Proyect Name"] = "Nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Franco Rudy"
    config._metadata["foo"] = "bar"


# It is hook for Delete/Modify Environment section of pytest HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # For default, the HTML Reports add this info, so we no need for this case.
    metadata.pop("Plugins", None)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == "call" or report.when == "setup":
#         # always add url to report
#         # extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             fileName="C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Screenshots\\" + report.nodeid.replace("::","_") + ".png"
#             captureScreenshot(fileName)
#             # only add additional html on failure
#             html = "<div><img src='%s' alt='screenshot style='width:304px;height:228px;' onclick='window.open(this.src) align='right' /></div>" % fileName
#             extra.append(pytest_html.extras.html(html))
#             report.extra = extra

# def captureScreenshot(name):
#     driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "Automation Report NopCommerce App"