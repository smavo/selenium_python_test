# Importar la libreria de webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.maximize_window()

# Acceder al sitio
driver.get("https://opensource-demo.orangehrmlive.com")
print(driver.title)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.XPATH, "//h6")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed...")

