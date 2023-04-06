import time
from selenium.webdriver.common.by import By
from POM.Locators.Locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # self.homepage_button_className = "oxd-userdropdown-tab"
        # self.homepage_logout_LinkText = "Logout"

    def HomeDashboard(self):
        self.driver.find_element(By.CLASS_NAME, Locators.homepage_button).click()
        time.sleep(2)

    def HomeLogout(self):
        self.driver.find_element(By.LINK_TEXT, Locators.homepage_logout).click()
        time.sleep(2)
