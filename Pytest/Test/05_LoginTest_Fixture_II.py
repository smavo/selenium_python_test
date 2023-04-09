import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest
from Pytest.Pages.LoginPage import LoginPage

tm = 1
driver = ""


@pytest.fixture(scope='module')
def setup_function_I():
    global driver
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)
    print("Iniciando nuestro Test")


@pytest.fixture(scope='module')
def setup_function_II():
    global driver
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)
    print("Iniciando nuestro Test")


def teardown_Function():
    print("============================== Test Finalizado ==============================")
    driver.close()
    driver.quit()


def test_Login_Chrome(setup_function_I):
    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "admin", 1)
    pl.Logout_Test()


def test_Login_Firefox(setup_function_II):
    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "admin", 1)
    # pl.Modulo_System_Inf()
    pl.Logout_Test()

