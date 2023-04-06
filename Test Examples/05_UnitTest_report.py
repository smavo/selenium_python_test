import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = ChromeOptions()
        cls.options.add_argument("--headless")
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

    @unittest.skip("This is a skipped test 1.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @classmethod
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @classmethod
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.skip("This is a skipped test 2.")
    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    @unittest.skip("This is a skipped test 3.")
    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

# python 05_UnitTest_report.py                --> Correr prueba + Reporte HTML
