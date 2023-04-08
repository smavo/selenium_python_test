
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from POM_2.Funciones.Funciones import Funciones_Globales
from Excel_Openpyxl import *

tg = 1

class base_test_Excel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Configuraciones para el navegador
        self.options = ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def test_example(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        fe = Fun_excel(driver)
        f.Navegar_T("https://demoqa.com/text-box", tg)
        ruta = "C://Users//Smavodev//Desktop//Selenium Python//Selenium_python//ExcelPath//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

        for r in range(2, filas+1):
            nombre = fe.readData(ruta, "Hoja1", r, 1)
            email = fe.readData(ruta, "Hoja1", r, 2)
            dir1 = fe.readData(ruta, "Hoja1", r, 3)
            dir2 = fe.readData(ruta, "Hoja1", r, 4)

            f.Texto_TYPE("id", "userName", nombre, tg)
            # f.Texto_ID("userName", nombre, tg)
            f.Texto_TYPE("id", "userEmail", email, tg)
            # f.Texto_ID("userEmail", email, tg)
            f.Texto_TYPE("id", "currentAddress", dir1, tg)
            # f.Texto_ID("currentAddress", dir1, tg)
            f.Texto_TYPE("id", "permanentAddress", dir2, tg)
            # f.Texto_ID("permanentAddress", dir2, tg)
            f.Button_TYPE("id", "submit", tg)

            e = f.Existe_Selector("id", "name", tg)
            if e == "Existe":
                print("El elemento se inserto correctamente")
                print("====================== SE FINALIZA LA EJECUCIÓN DE LA INSERCIÓN ======================")
                print("   ")
                fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se Inserto")
                fe.writeData(ruta, "Hoja1", r, 5, "Error")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
