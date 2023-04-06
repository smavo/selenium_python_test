import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def username_valid(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def password_valid(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def button_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        time.sleep(5)
