import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChomeOptions
from Pytest.Funciones.Funciones import Funciones_Globales_Pyest

tm = 1


def test_login_email_incorrecto():
    global driver
    # Configuraciones para el navegador
    options = ChomeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    f = Funciones_Globales_Pyest(driver)
    f.Navegar_T("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin", tm)

    f.Texto_TYPE("id", "Email", "adminS@yourstore.com", tm)
    f.Texto_TYPE("id", "Password", "admin", tm)
    f.Button_TYPE("xpath", "//button[@type='submit'][contains(.,'Log in')]", tm)

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

    f.Texto_TYPE("id", "Email", "admins", tm)
    f.Texto_TYPE("id", "Password", "admin", tm)
    f.Button_TYPE("xpath", " //button[@type='submit'][contains(.,'Log in')]", tm)

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

    f.Texto_TYPE("id", "Email", "", tm)
    f.Texto_TYPE("id", "Password", "admin", tm)
    f.Button_TYPE("xpath", " //button[@type='submit'][contains(.,'Log in')]", tm)

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

    f.Texto_TYPE("id", "Email", "admin@yourstore.com", tm)
    f.Texto_TYPE("id", "Password", "", tm)
    f.Button_TYPE("xpath", " //button[@type='submit'][contains(.,'Log in')]", tm)

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

    f.Texto_TYPE("id", "Email", "admin@yourstore.com", tm)
    f.Texto_TYPE("id", "Password", "demos", tm)
    f.Button_TYPE("xpath", " //button[@type='submit'][contains(.,'Log in')]", tm)

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

    f.Texto_TYPE("id", "Email", "admin@yourstore.com", tm)
    f.Texto_TYPE("id", "Password", "admin", tm)
    f.Button_TYPE("xpath", " //button[@type='submit'][contains(.,'Log in')]", tm)

    s1 = f.SEXPATH("//div/h1[contains(.,'Dashboard')]")
    s1 = s1.text
    print(s1)
    if s1 == "Dashboard":
        print("Login Exitoso")
    else:
        print("La prueba de Login es Incorrecto")

    f.Button_TYPE("xpath", "//a[@class='nav-link'][contains(.,'Logout')]", 1)
    f.cerrar_test()
