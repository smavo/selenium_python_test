# Importar la libreria de webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from POM_2.Pages.LoginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

URL_BASE = os.getenv('URL_PATH')
USR_TEST = os.getenv('USER_VALID')
PWD_TEST = os.getenv('PASS_VALID')

tm = 2


class base_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Configuraciones para el navegador
        self.options = ChomeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def test_sample(self):

        driver = self.driver
        f = LoginPage(driver)

        f.Navegar_URL(URL_BASE, tm)
        # f.Navegar_URL("https://www.saucedemo.com", tm)
        f.Login_Mixto(USR_TEST, PWD_TEST, tm)
        # f.Login_Mixto("standard_user", "secret_sauce", tm)
        f.Filtro_Ascendente_Mixto()
        f.Logout_mixto()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
