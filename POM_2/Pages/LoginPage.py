
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

    # ========= POM AUTOMATIZADO POR FUNCIONES GLOBALES POR COMPONENTES =========

    def Login_Mixto(self, USERNAME, PASSWORD, TIEMPO):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Texto_TYPE("id", "user-name", USERNAME, 1)
        f.Texto_TYPE("name", "password", PASSWORD, 1)
        f.Button_TYPE("id", "login-button", 2)
        # f.Button_Mixto("name", "login-button", 2)
        f.Tiempo_sleep(TIEMPO)

    def Filtro_Ascendente_Mixto(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Button_TYPE("class", "product_sort_container", 1)
        f.Button_TYPE("xpath", "//option[@value='za']", 1)
        f.Tiempo_sleep(3)

    def Logout_mixto(self):
        driver = self.driver
        f = Funciones_Globales(driver)

        f.Button_TYPE("class", "bm-burger-button", 1)
        f.Button_TYPE("xpath", "//a[@id='logout_sidebar_link']", 1)
        f.Tiempo_sleep(3)
        f.Fin_Test()
