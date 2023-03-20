from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    serv_obj = Service("C:\Pycharm2023\webdriver\chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver