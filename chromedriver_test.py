# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
driver = webdriver.Chrome(options=options)

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde Chrome")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()

# Más información sobre instalación de controladores del navegador
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# https://pypi.org/project/webdriver-manager/
