import time
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.homepage_button = "oxd-userdropdown-tab"
        self.homepage_logout = "Logout"

    def HomeDashboard(self):
        self.driver.find_element(By.CLASS_NAME, self.homepage_button).click()
        time.sleep(2)

    def HomeLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.homepage_logout).click()
        time.sleep(2)
