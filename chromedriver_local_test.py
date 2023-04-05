# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service = Service(executable_path=".\Drivers\chromedriver.exe")
service = Service(executable_path="./Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde Chrome")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()
