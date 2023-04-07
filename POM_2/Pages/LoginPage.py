
from POM_2.Funciones.Funciones import Funciones_Globales


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def Navegar_URL(self, URL,TIEMPO):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Navegar(URL)
        f.Tiempo_sleep(TIEMPO)

    def LoginSauce(self, USERNAME, PASSWORD, TIEMPO):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Texto_NAME("user-name", USERNAME, 1)
        f.Texto_NAME("password", PASSWORD, 1)
        f.Button_ID("login-button")
        f.Tiempo_sleep(TIEMPO)

    def filtro_Ascendente(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Button_CLASS_NAME("product_sort_container")
        f.Button_XPATH("//option[@value='za']")
        f.Tiempo_sleep(3)

    def Logout(self):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Button_CLASS_NAME("bm-burger-button")
        f.Button_XPATH("//a[@id='logout_sidebar_link']")
        f.Tiempo_sleep(3)
        f.Fin_Test()
