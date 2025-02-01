from selenium.webdriver.common.by import By
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def signup_button(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign").click()

    def enter_email_id(self, username="vinodkumar.31n@gmail.com"):
        self.driver.find_element(By.ID, "login_field").send_keys(username)

    def enter_password(self):
        self.driver.find_element(By.ID, "password").send_keys("VINUvinu@123")

    def click_signin(self):
        self.driver.find_element(By.NAME, 'commit').click()

    def get_invalid_login_error_txt(self):
      error_message = self.driver.find_element(By.XPATH,"//div/div/div/div/div[@class= 'js-flash-alert']").text()
      print(error_message)