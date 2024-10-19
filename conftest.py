import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    return driver


# This will give the value of CLI hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# # Pytest HTML Report
# # Hook for adding environment info into html
# def pytest_Configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customer'
#     config._metadata['Tester'] = 'Vikram'


# # Hook for delete / Modify Environment info to html Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)
