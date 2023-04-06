import time
from selenium.webdriver.common.by import By
from POM.Locators.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # self.username_textbox_name = Locators.username_textbox
        # self.password_textbox_name = Locators.password_textbox
        # self.login_button_xpath = Locators.login_button

    def username_valid(self, username):
        self.driver.find_element(By.NAME, Locators.username_textbox).send_keys(username)

    def password_valid(self, password):
        self.driver.find_element(By.NAME, Locators.password_textbox).send_keys(password)

    def button_login(self):
        self.driver.find_element(By.XPATH, Locators.login_button).click()
        time.sleep(5)
