# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = EdgeOptions()
options.add_argument("--headless")
driver = webdriver.Edge(options=options)
# driver.set_page_load_timeout(2)

# Maximizar el navegador
# driver.maximize_window()

# Acceder al sitio
driver.get("https://google.com")
print(driver.title)
driver.find_element(By.NAME, "q").send_keys("Smavodev.com")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()
print("Test Completed Edge")

