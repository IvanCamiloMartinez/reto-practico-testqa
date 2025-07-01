import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# Configurar el servicio del driver
service = Service(executable_path="C:\Drivers\chromedriver.exe", service_log_path=os.devnull)
driver = webdriver.Chrome(service=service)

# 1. Abrir la página
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
time.sleep(2)
driver.save_screenshot("01-homepage.png") 

# 2. Hacer clic en 'Make Appointment'
driver.find_element(By.ID, "btn-make-appointment").click()
time.sleep(2)
driver.save_screenshot("02-login-form.png") 

# 3. Iniciar sesión
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
time.sleep(1)
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
time.sleep(1)
driver.find_element(By.ID, "btn-login").click()
time.sleep(5)
driver.save_screenshot("03-login-exitoso.png")

# 4. Llenar formulario de cita
dropdown = Select(driver.find_element(By.ID, "combo_facility"))
dropdown.select_by_value("Hongkong CURA Healthcare Center")
time.sleep(1)

driver.find_element(By.ID, "chk_hospotal_readmission").click()
time.sleep(1)

driver.find_element(By.ID, "radio_program_medicaid").click()
time.sleep(1)

driver.find_element(By.ID, "txt_visit_date").send_keys("06/05/2025")
time.sleep(1)

driver.find_element(By.ID, "txt_comment").send_keys(
    "Este es un menaje de prueba para la automatización de páginas web con Selenium y Python para el segundo reto práctico de Lite Thinking."
)
time.sleep(1)

driver.save_screenshot("04-formulario-llenado.png")
# 5. Enviar el formulario
driver.find_element(By.ID, "btn-book-appointment").click()
time.sleep(2)
driver.save_screenshot("05-confirmacion-cita.png")

# 6. Volver a inicio
driver.find_element(By.CLASS_NAME, "btn-default").click()
time.sleep(1)
driver.save_screenshot("06-vuelta-dashboard.png")

# 7. Logout
driver.find_element(By.ID, "menu-toggle").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(2)
driver.save_screenshot("07-logout.png")
# 8. Cerrar navegador
driver.close()

import os
print("Capturas guardadas en:", os.getcwd())


