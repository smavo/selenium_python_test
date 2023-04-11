from Funciones.Funciones import Funciones_Globales_Pyest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def Navegar_URL(self, URL, TIEMPO):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)

        f.Navegar(URL)
        f.Tiempo_sleep(TIEMPO)

    def Login_Test(self, USERNAME, PASSWORD, TIEMPO):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)

        f.Texto_TYPE("id", "Email", USERNAME, TIEMPO)
        f.Texto_TYPE("id", "Password", PASSWORD, TIEMPO)
        f.Button_TYPE("xpath", "//button[@type='submit'][contains(.,'Log in')]", 1)
        f.Tiempo_sleep(3)

    def Logout_Test(self):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)
        f.Button_TYPE("xpath", "//a[@class='nav-link'][contains(.,'Logout')]", 1)
        f.cerrar_test()

    def Login_Test_II(self, USERNAME, PASSWORD, TIEMPO):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)

        f.Texto_TYPE("name", "username", USERNAME, TIEMPO)
        f.Texto_TYPE("name", "password", PASSWORD, TIEMPO)
        f.Button_TYPE("xpath", "//button[@type='submit'][contains(.,'Login')]", 1)
        f.Tiempo_sleep(3)

    def Logout_Test_II(self):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)
        f.Button_TYPE("xpath", "//span[@class='oxd-userdropdown-tab']", 1)
        f.Button_TYPE("xpath", "//a[contains(.,'Logout')]", 2)
        f.cerrar_test()

    def Modulo_Seleccionado(self, menu):
        driver = self.driver
        f = Funciones_Globales_Pyest(driver)
        f.Button_TYPE("xpath", "//a[contains(.,'" + menu + "')]", 3)

    def valid_assert_xpath(self, selector):
        driver = self.driver
        valid = driver.find_element(By.XPATH, "//a[contains(.,'" + selector + "')]").text
        print(valid)

        if valid == selector:
            print("===================================")
            print("Estas en el Menu de " + selector)
            print("===================================")
            assert valid == selector, "Menu " + selector + "seleccionado correctamente"
        else:
            assert valid != selector, "No es el Menu especificado"


