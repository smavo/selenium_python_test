import pytest
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest

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
