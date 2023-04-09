import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


# https://www.lambdatest.com/blog/handling-errors-and-exceptions-in-selenium-python/

class Funciones_Globales_Pyest:

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
        print("Accediendo a la URL: " + str(URL))

    def Navegar_T(self, URL, Tiempo):
        self.driver.get(URL)
        self.driver.maximize_window()
        print("Accediendo a la URL: " + str(URL))
        t = time.sleep(Tiempo)
        return t

    def cerrar_test(self):
        time.sleep(3)
        print("============================= Se finalizo la prueba =============================")
        print(" ")
        self.driver.close()
        self.driver.quit()

    # =================================== FUNCIONES POR COMPONENTES ===================================

    # Texto: XPATH, ID, NAME, CLASS_NAME, CSS_SELECTOR, TAG_NAME
    def Texto_XPath(self, xpath, texto, tiempo):
        try:
            value = self.driver.find_element(By.XPATH, xpath)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(xpath, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + xpath)

    def Texto_ID(self, ID, texto, tiempo):
        try:
            value = self.driver.find_element(By.ID, ID)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(ID, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + ID)

    def Texto_NAME(self, NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.NAME, NAME)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(NAME, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + NAME)

    def Texto_CLASS_NAME(self, CLASS_NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(CLASS_NAME, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + CLASS_NAME)

    def Texto_CSS_SELECTOR(self, CSS_SELECTOR, texto, tiempo):
        try:
            value = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(CSS_SELECTOR, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + CSS_SELECTOR)

    def Texto_TAG_NAME(self, TAG_NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.TAG_NAME, TAG_NAME)
            value.clear()
            value.send_keys(texto)
            print("Ingresando datos en el campo --> {} el texto --> {} ".format(TAG_NAME, texto))
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + TAG_NAME)

    # BUTTON: XPATH, ID, NAME, CLASS_NAME, CSS_SELECTOR, TAG_NAME
    def Button_XPATH(self, XPATH):
        try:
            value = self.driver.find_element(By.XPATH, XPATH)
            value.click()
            print("Damos click en el campo --> {}".format(XPATH))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + XPATH)

    def Button_ID(self, ID):
        try:
            value = self.driver.find_element(By.ID, ID)
            value.click()
            print("Damos click en el campo --> {}".format(ID))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + ID)

    def Button_NAME(self, NAME):
        try:
            value = self.driver.find_element(By.NAME, NAME)
            value.click()
            print("Damos click en el campo --> {}".format(NAME))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + NAME)

    def Button_CLASS_NAME(self, CLASS_NAME):
        try:
            value = self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
            value.click()
            print("Damos click en el campo --> {}".format(CLASS_NAME))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + CLASS_NAME)

    def Button_CSS_SELECTOR(self, CSS_SELECTOR):
        try:
            value = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            value.click()
            print("Damos click en el campo --> {}".format(CSS_SELECTOR))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + CSS_SELECTOR)

    def Button_TAG_NAME(self, TAG_NAME):
        try:
            value = self.driver.find_element(By.TAG_NAME, TAG_NAME)
            value.click()
            print("Damos click en el campo --> {}".format(TAG_NAME))
            time.sleep(2)
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: " + TAG_NAME)

    # SELECTOR: XPATH
    # https://www.selenium.dev/documentation/webdriver/elements/information/
    def Select_XPath(self, XPATH, TEXTO, TIEMPO):
        try:
            sel = Select(self.driver.find_element(By.XPATH, XPATH))
            time.sleep(2)
            sel.select_by_visible_text(TEXTO)
            time.sleep(5)
            print("El campo seleccionado es: --> {}".format(TEXTO))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + XPATH)

    def Select_XPath_Tipo(self, XPATH, TIPO, DATO, TIEMPO):
        try:
            sel = Select(self.driver.find_element(By.XPATH, XPATH))
            time.sleep(1)

            if TIPO == "text":
                sel.select_by_visible_text(DATO)
            elif TIPO == "value":
                sel.select_by_value(DATO)
            elif TIPO == "index":
                sel.select_by_index(DATO)

            time.sleep(1)

            print("El campo seleccionado es: --> {}".format(DATO))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + XPATH)

    # CHECK_BOX: XPATH, ID, CLASS_NAME, NAME
    def Check_Xpath(self, XPATH, TIEMPO):
        try:
            value = self.driver.find_element(By.XPATH, XPATH)
            # value = self.driver.execute_script("arguments[0].scrollIntoView()", value)
            value.click()
            print("Click en el elemento: --> {}".format(XPATH))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + XPATH)

    def Check_ID(self, ID, TIEMPO):
        try:
            value = self.driver.find_element(By.ID, ID)
            value.click()
            print("Click en el elemento: --> {}".format(ID))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + ID)

    def Check_CLASS_NAME(self, CLASS_NAME, TIEMPO):
        try:
            value = self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
            value.click()
            print("Click en el elemento: --> {}".format(CLASS_NAME))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + CLASS_NAME)

    def Check_NAME(self, NAME, TIEMPO):
        try:
            value = self.driver.find_element(By.NAME, NAME)
            value.click()
            print("Click en el elemento: --> {}".format(NAME))
            time.sleep(TIEMPO)

        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento: --> " + NAME)

    def Check_XPath_Multiple(self, TIEMPO, *args):
        try:
            for nun in args:
                value = self.driver.find_element(By.XPATH, nun)
                value.click()
                print("Click en el elemento: --> {}".format(nun))
                time.sleep(TIEMPO)
                return TIEMPO

        except NoSuchElementException as ex:
            for nun in args:
                print(ex.msg)
                print("No se encontró el elemento: --> " + nun)

    # =================================== FUNCIONES GLOBALES POR COMPONENTES ===================================

    # TEXTO MIXTO: XPATH, ID, NAME, CLASS_NAME
    def Texto_TYPE(self, tipo, selector, texto, tiempo):
        if tipo == "xpath":
            try:
                value = self.driver.find_element(By.XPATH, selector)
                value.clear()
                value.send_keys(texto)
                print("Ingresando datos en el campo --> {} el texto --> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)

        elif tipo == "id":
            try:
                value = self.driver.find_element(By.ID, selector)
                value.clear()
                value.send_keys(texto)
                print("Ingresando datos en el campo --> {} el texto --> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)

        elif tipo == "name":
            try:
                value = self.driver.find_element(By.NAME, selector)
                value.clear()
                value.send_keys(texto)
                print("Ingresando datos en el campo --> {} el texto --> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)

        elif tipo == "class":
            try:
                value = self.driver.find_element(By.CLASS_NAME, selector)
                value.clear()
                value.send_keys(texto)
                print("Ingresando datos en el campo --> {} el texto --> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)

    # BUTTON MIXTO: XPATH, ID, NAME, CLASS_NAME
    def Button_TYPE(self, TIPO, SELECTOR, TIEMPO):
        if TIPO == "xpath":
            try:
                value = self.driver.find_element(By.XPATH, SELECTOR)
                value.click()
                print("Damos click en el campo --> {}".format(SELECTOR))
                time.sleep(TIEMPO)
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + SELECTOR)

        elif TIPO == "id":
            try:
                value = self.driver.find_element(By.ID, SELECTOR)
                value.click()
                print("Damos click en el campo --> {}".format(SELECTOR))
                time.sleep(TIEMPO)
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + SELECTOR)

        elif TIPO == "name":
            try:
                value = self.driver.find_element(By.NAME, SELECTOR)
                value.click()
                print("Damos click en el campo --> {}".format(SELECTOR))
                time.sleep(TIEMPO)
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + SELECTOR)

        elif TIPO == "class":
            try:
                value = self.driver.find_element(By.CLASS_NAME, SELECTOR)
                value.click()
                print("Damos click en el campo --> {}".format(SELECTOR))
                time.sleep(TIEMPO)
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + SELECTOR)

    def Existe_Selector(self, tipo, selector, tiempo):
        if tipo == "xpath":
            try:
                value = self.driver.find_element(By.XPATH, selector)
                print("El elemento {} -> Existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)
                return "No existe"

        elif tipo == "id":
            try:
                value = self.driver.find_element(By.ID, selector)
                print("El elemento {} -> Existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"

            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)
                return "No existe"

        elif tipo == "name":
            try:
                value = self.driver.find_element(By.NAME, selector)
                print("El elemento {} -> Existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"

            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)
                return "No existe"

        elif tipo == "class":
            try:
                value = self.driver.find_element(By.CLASS_NAME, selector)
                print("El elemento {} -> Existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"

            except NoSuchElementException as ex:
                print(ex.msg)
                print("No se encontró el elemento: " + selector)
                return "No existe"

    # Seleccionar elemento por Xpath
    def SEXPATH(self, selector):
        value = self.driver.find_element(By.XPATH, selector)
        return value

    # Seleccionar elemento por ID
    def SEID(self, selector):
        value = self.driver.find_element(By.XPATH, selector)
        return value
