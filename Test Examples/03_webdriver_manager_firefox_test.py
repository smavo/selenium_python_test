# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.set_page_load_timeout(2)

# Maximizar el navegador
driver.maximize_window()

# Acceder al sitio
driver.get("https://google.com")
print(driver.title)
driver.find_element(By.NAME, "q").send_keys("Smavodev.com")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()
print("Test Completed Firefox")


# https://pypi.org/project/webdriver-manager/
# https://github.com/SergeyPirogov/webdriver_manager
# Ruta donde se guardan los driver descargados: C:\Users\Smavodev\.wdm
