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

        f.Navegar("https://www.saucedemo.com")

        f.Texto_NAME("user-name", "standard_user", 1)
        f.Texto_NAME("password", "secret_sauce", 1)
        f.Button_ID("login-button")
        f.Tiempo_sleep(3)
        f.Button_CLASS_NAME("product_sort_container")
        f.Button_XPATH("//option[@value='za']")
        f.Tiempo_sleep(3)
        # f.Select_XPath_Tipo("//div/span/select[@class='product_sort_container']", "value", "za", 2)
        # f.Select_XPath_Tipo("//div/span/select[@class='product_sort_container']", "text", "Price (low to high)", 2)
        # f.Select_XPath_Tipo("//div/span/select[@class='product_sort_container']", "index", "0", 2)
        f.Button_CLASS_NAME("bm-burger-button")
        f.Button_XPATH("//a[@id='logout_sidebar_link']")
        f.Tiempo_sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
