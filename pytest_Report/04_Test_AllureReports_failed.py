import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Funciones.Funciones import Funciones_Globales_Pyest
from allure_commons.types import AttachmentType
from LoginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

URL_BASE = os.getenv('URL_PATH')
USR_TEST = os.getenv('USER_VALID')
PWD_TEST = os.getenv('PASS_VALID')

tm = 3
driver = ""


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope='module')
def setup_function_I():
    global driver
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # service = Service(executable_path="../Drivers/chromedriver.exe")
    # driver = webdriver.Chrome(service=service)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T(URL_BASE, tm)
    print("Iniciando nuestro Test")


def teardown_Function():
    print("============================== Test Finalizado ==============================")
    driver.close()
    driver.quit()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.skip
# @pytest.mark.login
def test_Login_Chrome_I(setup_function_I):
    pl = LoginPage(driver)
    # pl.Login_Test_II("Admin", "admin123", 1)
    pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    pl.Modulo_Seleccionado("My Info")
    pl.Modulo_Seleccionado("Leave")
    pl.Logout_Test_II()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.skip
# @pytest.mark.login
def test_Login_Chrome_II(setup_function_I):
    pl = LoginPage(driver)
    pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    # pl.Login_Test_II("Admin", "admin123", 1)
    pl.Modulo_Seleccionado("Leave")
    pl.Modulo_Seleccionado("PIM")
    pl.Logout_Test_II()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.skip
# @pytest.mark.login
def test_Login_Firefox_III(setup_function_I):
    pl = LoginPage(driver)
    pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    # pl.Login_Test_II("Admin", "admin123", 1)
    pl.Modulo_Seleccionado("Leave")
    pl.Logout_Test_II()

# esclamacion
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.run
def test_Login_Chrome_IV(setup_function_I):
    pl = LoginPage(driver)
    # pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    pl.Login_Test_II("Admin", "admin12334", 1)
    pl.Modulo_Seleccionado("xcczxc")
    pl.Logout_Test_II()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.skip
# @pytest.mark.login
def test_Login_Chrome_V(setup_function_I):
    pl = LoginPage(driver)
    # pl.Login_Test_II(USR_TEST, PWD_TEST, 1)
    pl.Login_Test_II("Admin", "admin123", 1)
    pl.Modulo_Seleccionado("Directory")
    pl.Logout_Test_II()


# Ejecutar en consola + Allure Reports
# Carpeta raíz en este caso: C:\Users\Smavodev\Desktop\Selenium Python\Selenium_python\pytest_Report
# pytest .\04_Test_AllureReports_failed.py --alluredir="./allurereports"
# Ejecutar reportes: allure serve .\allurereports
