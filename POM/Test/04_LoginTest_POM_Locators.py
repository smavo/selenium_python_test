# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import unittest
from POM.Pages.LoginPageLocators import LoginPage
from POM.Pages.HomePageLocators import HomePage


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

        homepage = HomePage(driver)
        homepage.HomeDashboard()
        homepage.HomeLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")


if __name__ == '__main__':
    unittest.main()
