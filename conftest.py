from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import datetime
import pytest
import logging
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    executor_url = "http:/localhost/administration/"

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        option = Options()
        driver = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        option = FirefoxOptions()
        driver = webdriver.Firefox(options=option)
    else:
        raise Exception("Driver not supported")

    allure.attach(
        name=driver.session_id,
        body=driver.current_url,
        attachment_type=allure.attachment_type.JSON,
    )

    driver.maximize_window()
    driver.get(executor_url)
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
