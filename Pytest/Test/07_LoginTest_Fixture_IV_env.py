import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest
from Pytest.Pages.LoginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

URL_BASE = os.getenv('URL_PATH')
USR_TEST = os.getenv('USER_VALID')
PWD_TEST = os.getenv('PASS_VALID')

tm = 1
driver = ""


@pytest.fixture(scope='module')
def setup_function_I():
    global driver
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T(URL_BASE, tm)
    print("Iniciando nuestro Test")


@pytest.fixture(scope='module')
def setup_function_II():
    global driver
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    f = Funciones_Globales_Pyest(driver)
    # f.Navegar_T("https://opensource-demo.orangehrmlive.com/", tm)
    f.Navegar_T(URL_BASE, tm)
    print("Iniciando nuestro Test")


def teardown_Function():
    print("============================== Test Finalizado ==============================")
    driver.close()
    driver.quit()


@pytest.mark.run
@pytest.mark.login
def test_Login_Chrome(setup_function_I):
    pl = LoginPage(driver)
    # pl.Login_Test_II("Admin", "admin123", 1)
    pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    pl.Modulo_Seleccionado("My Info")
    pl.Logout_Test_II()


@pytest.mark.skip
@pytest.mark.menu
def test_Login_Firefox(setup_function_II):
    pl = LoginPage(driver)
    pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    # pl.Login_Test_II("Admin", "admin123", 1)
    pl.Modulo_Seleccionado("Leave")
    pl.Logout_Test_II()

