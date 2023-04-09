from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest
from Pytest.Pages.LoginPage import LoginPage

tm = 1
driver = ""


def setup_function(function):
    global driver
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)
    print("Iniciando nuestro Test")


def teardown_Function(function):
    print("============================== Test Finalizado ==============================")
    driver.close()
    driver.quit()


def test_Login_Success():
    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "admin", 1)
    pl.Logout_Test()


def test_Login_Failed():
    pl = LoginPage(driver)
    f = Funciones_Globales_Pyest(driver)
    pl.Login_Test("test@yourstore.com", "admin", 1)
    e1 = f.SEXPATH("// li[contains(.,'No customer account found')]")
    e1 = e1.text
    print(e1)
    if e1 == "No customer account found":
        print("Prueba de validación de Cuenta no encontrada fue exitosa")
    else:
        print("La prueba de validación es incorrecta")

