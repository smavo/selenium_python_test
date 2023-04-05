# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
# driver.set_page_load_timeout(3)

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
print("Test Completed Chrome")

