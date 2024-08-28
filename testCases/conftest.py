from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("------------Launching the chrome browser..........")
    elif browser == 'firefox':
        print("------------Launching the firefox browser...........")
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching the firefox browser...........")
    else:
        driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# pytest html-report
# it is hooks for adding environment info to HTLM Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'MEtutors'
#     config._metadata['Module Name'] = 'Student'
#     config._metadata['Tester'] = 'ZAPTA'


# it is hooks fpr delete/modify environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Py_Home", None)
#     metadata.pop("Plugins", None)
