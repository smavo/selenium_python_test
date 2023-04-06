# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# service = Service(executable_path=".\Drivers\chromedriver.exe")
service = Service(executable_path="../Drivers/msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde Edge")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()
