# Importar la libreria de webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from POM_2.Funciones.Funciones import Funciones_Globales
from POM_2.Pages.LoginPage import LoginPage


class base_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Configuraciones para el navegador
        self.options = ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def test_sample(self):
        # driver = self.driver
        # f = Funciones_Globales(driver)

        # f.Navegar("https://www.saucedemo.com")
        # f.Navegar_T("https://www.saucedemo.com", 2)
        # f.Tiempo_sleep(2)

        # f.Texto_XPath("//input[@id='user-name']", "standard_user", 2)
        # f.Texto_ID("password", "secret_sauce", 2)
        # f.Button_ID("login-button")
        # f.Tiempo_sleep(2)

        driver = self.driver
        pl = LoginPage(driver)
        pl.Navegar_URL("https://www.saucedemo.com", 2)
        pl.LoginSauce("standard_user", "secret_sauce", 2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
