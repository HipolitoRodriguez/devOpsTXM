import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Fixture para configurar y cerrar el navegador
@pytest.fixture(scope="module")
def driver():
    # Configura el navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Cargar la URL (solo una vez antes de cada prueba)
    url = "http://localhost:9090/"
    driver.get(url)
    yield driver  # Esto devuelve el driver a las funciones de prueba
    driver.quit()  # Cierra el navegador al finalizar la prueba

# Prueba para agregar un empleado
def test_agregar_empleado(driver):
    # Paso 1: Hacer clic en "Add Employee"
    driver.find_element(By.XPATH, "//a[text()=' Add Employee ']").click()
    time.sleep(2)  # Evita usar sleeps; preferir esperas explícitas

    # Paso 2: Llenar los campos del formulario
    driver.find_element(By.ID, "firstName").send_keys("Aron")
    driver.find_element(By.ID, "lastName").send_keys("Acosta")
    driver.find_element(By.ID, "email").send_keys("aron_acosta@hotmail.com")

    # Paso 3: Guardar el empleado
    driver.find_element(By.XPATH, "//button[text()=' Save Employee']").click()
    time.sleep(5)  # También, evita este sleep

def test_actualizar_empleado(driver):
    # Actualizar Nombre empleado
    driver.find_element(By.XPATH,"//tr[td[1][text()='Aron']]/td/a[contains(text(), 'Update')]").click()
    time.sleep(2)
    campoNombre=driver.find_element("id", "firstName")
    campoNombre.clear()
    campoNombre.send_keys("Aron Arturo")


    # Actualizar Apellido empleado
    campoApellido=driver.find_element("id", "lastName")
    campoApellido.clear()
    campoApellido.send_keys("Acosta Martinez")

    # Actualizar mail empleado
    campoEmail=driver.find_element("id", "email")
    campoEmail.clear()
    campoEmail.send_keys("aron_acosta_update@hotmail.com")
    driver.find_element(By.XPATH,"//button[text()=' Update Employee']").click()
    time.sleep(5)

def test_borrar_empleado(driver):
    # Borrar el empleado
    driver.find_element(By.XPATH,"//tr[td[1][text()='Aron Arturo']]/td/a[contains(text(), 'Delete')]").click()
    time.sleep(5)