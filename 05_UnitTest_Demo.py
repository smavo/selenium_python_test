import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class testUnitSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = ChromeOptions()
        # cls.options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=cls.options)

    @classmethod
    def test_search(cls):
        cls.driver.get("https://google.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

        x = cls.driver.title
        print(x)

        cls.driver.find_element(By.NAME, "q").send_keys("Smavodev.com")
        cls.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        cls.driver.implicitly_wait(2)
        x = cls.driver.title
        print(x)
        # cls.assertEquals(x, "Smavodev.com - Buscar con Google")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed Chrome")


if __name__ == '__main__':
    unittest.main()

# Correr en consola
# python -m unittest 05_UnitTest_Demo.py    --> Correr solo prueba unitaria

