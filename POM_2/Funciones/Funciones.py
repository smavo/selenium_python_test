import time
from selenium.webdriver.common.by import By


class Funciones_Globales:

    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Welcome a Page Object Model")

    def Tiempo_sleep(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def Navegar(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()

    def Navegar_T(self, URL, Tiempo):
        self.driver.get(URL)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def Texto_XPath(self, xpath, texto, tiempo):
        value = self.driver.find_element(By.XPATH, xpath)
        value.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def Texto_ID(self, ID, texto, tiempo):
        value = self.driver.find_element(By.ID, ID)
        value.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def Button_ID(self, value):
        value = self.driver.find_element(By.ID, value)
        value.click()
