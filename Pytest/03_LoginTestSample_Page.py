import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest
from Pages.LoginPage import LoginPage

tm = 1
global driver


def test_login_email_incorrecto():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("test@yourstore.com", "admin", 1)

    e1 = f.SEXPATH("// li[contains(.,'No customer account found')]")
    e1 = e1.text
    print(e1)
    if e1 == "No customer account found":
        print("Prueba de validación de Cuenta no encontrada fue exitosa")
    else:
        print("La prueba de validación es incorrecta")

    f.cerrar_test()


def test_login_email_formato_error():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("admins", "admin", 1)

    e1 = f.SEXPATH("//span[contains(@id,'Email-error')]")
    e1 = e1.text
    print(e1)
    if e1 == "Wrong email":
        print("Prueba de validación de Email incorrecto es exitoso")
    else:
        print("La prueba de validación es incorrecta")

    f.cerrar_test()


def test_login_email_empty():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("", "admin", 1)

    e1 = f.SEXPATH("//span[@id='Email-error']")
    e1 = e1.text
    print(e1)
    if e1 == "Please enter your email":
        print("Prueba de validación de Email vacío es exitosa")
    else:
        print("La prueba de validación es incorrecta")

    f.cerrar_test()


def test_login_pasword_empty():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "", 1)

    e1 = f.SEXPATH("//li[contains(.,'The credentials provided are incorrect')]")
    e1 = e1.text
    print(e1)
    if e1 == "The credentials provided are incorrect":
        print("Prueba de validación de password vacío es Exitosa")
    else:
        print("La prueba de validación es incorrecta")

    f.cerrar_test()


def test_login_pasword_erroneo():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "demotest", 1)

    e1 = f.SEXPATH("//li[contains(.,'The credentials provided are incorrect')]")
    e1 = e1.text
    print(e1)
    if e1 == "The credentials provided are incorrect":
        print("Prueba de validación de Password Incorrecto fue exitosa")
    else:
        print("La prueba de validación es incorrecta")

    f.cerrar_test()


def test_login_passed():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    pl = LoginPage(driver)
    pl.Login_Test("admin@yourstore.com", "admin", 1)

    s1 = f.SEXPATH("//div/h1[contains(.,'Dashboard')]")
    s1 = s1.text
    print(s1)
    if s1 == "Dashboard":
        print("Login Exitoso")
    else:
        print("La prueba de Login es Incorrecto")

    pl.Logout_Test()
