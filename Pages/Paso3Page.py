from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
import time

class Paso3Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.nombre = (By.ID, 'firstName')
        self.apellido = (By.ID, 'lastName')
        self.tipoDNI = (By.ID, 'id_type')
        self.dni = (By.ID, 'id_value')
        self.diaNacimiento = (By.ID, 'day_select')
        self.mesNacimiento = (By.ID, 'month_select')
        self.anioNacimiento = (By.ID, 'year_select')                
        self.generoMasculino = (By.XPATH, '//label[contains(text(), "Masculino")]')
        self.codArea = (By.ID, 'codphone')
        self.telefono = (By.ID, 'phone')
        self.email = (By.ID, 'email')
        self.calle = (By.ID, 'street_name')
        self.altura = (By.ID, 'street_number')
        self.piso = (By.ID, 'floor')
        self.dpto = (By.ID, 'room')
        self.codigoPostal = (By.ID, 'zip_code')
        self.terminos = (By.ID, 'terms-conditions')
        self.continuar = (By.ID, 'continue')
     
    def completarPaso3(self):
        self.driver.find_element(*self.nombre).send_keys("Romina")
        self.driver.find_element(*self.apellido).send_keys("Milillo")
        
        Select(self.driver.find_element(*self.tipoDNI)).select_by_value("DNI")
        self.driver.find_element(*self.dni).send_keys("34503338")

        Select(self.driver.find_element(*self.diaNacimiento)).select_by_value("28")
        Select(self.driver.find_element(*self.mesNacimiento)).select_by_visible_text("Marzo")
        Select(self.driver.find_element(*self.anioNacimiento)).select_by_value("1950")

        self.driver.find_element(*self.generoMasculino).click()

        self.driver.find_element(*self.codArea).send_keys("11")
        self.driver.find_element(*self.telefono).send_keys("1566778899")
        self.driver.find_element(*self.email).send_keys("joseperez@gmail.com")
        self.driver.find_element(*self.calle).send_keys("Laprida")
        self.driver.find_element(*self.altura).send_keys("2020")
        self.driver.find_element(*self.piso).send_keys("4")
        self.driver.find_element(*self.dpto).send_keys("2")
        self.driver.find_element(*self.codigoPostal).send_keys("1888")

        self.driver.find_element(*self.terminos).click()

        breakpoint()   

    def irPaso4(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar)).click()
        time.sleep(5)


