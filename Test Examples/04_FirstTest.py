# Importar la libreria de webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# service = Service(executable_path=".\Drivers\chromedriver.exe")
service = Service(executable_path="../Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(5)

# Maximizar el navegador
driver.maximize_window()

# Acceder al sitio
driver.get("https://google.com")

driver.find_element(By.NAME, "q").send_keys("Smavodev.com")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
print(driver.title)
time.sleep(2)
driver.close()
driver.quit()
