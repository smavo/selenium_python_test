# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import unittest
from POM.Pages.LoginPage import LoginPage
from POM.Pages.HomePage import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = ChromeOptions()
        # cls.options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=cls.options)

    def test_login_valid(self):
        driver = self.driver

        # Acceder al sitio
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(6)
        # print(self.driver.title)

        login = LoginPage(driver)
        login.username_valid("Admin")
        login.password_valid("admin123")
        login.button_login()

        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # self.driver.find_element(By.XPATH, "//h6")
        # time.sleep(5)

        homepage = HomePage(driver)
        homepage.HomeDashboard()
        homepage.HomeLogout()

        # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        # time.sleep(2)
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")


if __name__ == '__main__':
    unittest.main()
