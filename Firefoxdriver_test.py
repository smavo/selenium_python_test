# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde firefox")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()
