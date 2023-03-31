# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

options = EdgeOptions()
driver = webdriver.Edge(options=options)

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde Edge")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()