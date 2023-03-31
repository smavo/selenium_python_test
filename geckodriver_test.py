# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm")

# Acceder a la url https://demoqa.com/
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()