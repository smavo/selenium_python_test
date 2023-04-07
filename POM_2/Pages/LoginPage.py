
from POM_2.Funciones.Funciones import Funciones_Globales


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def LoginSauce(self, URL, USERNAME, PASSWORD, TIEMPO):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Navegar(URL)
        f.Tiempo_sleep(TIEMPO)

        f.Texto_XPath("//input[@id='user-name']", USERNAME, TIEMPO)
        f.Texto_ID("password", PASSWORD, TIEMPO)
        f.Button_ID("login-button")
        f.Tiempo_sleep(TIEMPO)
