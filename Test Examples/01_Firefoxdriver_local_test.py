# Importar la libreria de webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# https://pypi.org/project/webdriver-manager/

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# service = Service(executable_path=".\Drivers\chromedriver.exe")

# Maximizar el navegador
driver.maximize_window()

print("Bienvenido a Pycharm desde Firefox")

# Acceder a la url
driver.get("https://www.saucedemo.com/")

# Imprimir
print(driver.title)

# Finalizar el driver
driver.close()
