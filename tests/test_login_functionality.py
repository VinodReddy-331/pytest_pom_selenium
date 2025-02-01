import time

import pytest
from selenium.webdriver.common.by import By
from src.pages.loginpage import LoginPage


class TestLoginFunctionality:
    def test_validate_title(self, browser):
        title = browser.title
        assert title == "GitHub · Build and ship software on a single, collaborative platform · GitHub", f"Title is not matching"

    def test_invalidate_signin(self, browser):
        self.loginObj = LoginPage(browser)
        self.loginObj.signup_button()
        self.loginObj.enter_email_id("test")
        self.loginObj.enter_password()
        self.loginObj.click_signin()
        time.sleep(5)
        assert self.loginObj.get_invalid_login_error_txt() == "Incorrect username or password."

    def test_validate_signin(self, browser):
        self.loginObj = LoginPage(browser)
        self.loginObj.signup_button()
        self.loginObj.enter_email_id()
        self.loginObj.enter_password()
        self.loginObj.click_signin()
        assert browser.title == "GitHub"


