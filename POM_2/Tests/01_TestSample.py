# Importar la libreria de webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from POM_2.Funciones.Funciones import Funciones_Globales


class base_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Configuraciones para el navegador
        self.options = ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def test_sample(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.saludos()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
