import time

import pytest
from selenium import webdriver
from pytest import fixture


# @pytest.fixture(scope="function")  # If scope is function then it will launch for every test
@pytest.fixture(scope="class")  # If scope is class then it will launch only once for the class
def browser():
    driver = webdriver.Chrome()
    driver.get("https://github.com/")
    driver.maximize_window()
    time.sleep(5)
    yield driver  # Provide the driver object to the tests
    driver.close()  # Closes the Webdriver After the tests are completed.
