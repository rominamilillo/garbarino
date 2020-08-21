from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
from selenium.webdriver import ActionChains
import csv

class Paso3Page(object):
    def __init__(self, driver):
        self.driver = driver
        #self.nombre = (By.ID, 'firstName')
        #self.apellido = (By.ID, 'lastName')
        #self.tipoDNI = (By.ID, 'id_type')
        #self.dni = (By.ID, 'id_value')
        #self.diaNacimiento = (By.ID, 'day_select')
        #self.mesNacimiento = (By.ID, 'month_select')
        #self.añoNacimiento = (By.ID, 'year_select')
        #self.generoMasculino = (By.ID, 'masculino')
        #self.generoFemenino = (By.ID, 'femenino')
        #self.codArea = (By.ID, 'codphone')
        #self.telefono = (By.ID, 'phone')
        #self.email = (By.ID, 'email')
        #self.calle = (By.ID, 'street_name')
        #self.altura = (By.ID, 'street_number')
        #self.piso = (By.ID, 'floor')
        #self.dpto = (By.ID, 'room')
        #self.codigoPostal = (By.ID, 'zip_code')
        #self.terminos = (By.ID, 'terms-conditions')
        self.continuar = (By.ID, 'continue')
     
    def completarPaso3(self):
        self.driver.find_element_by_id('firstName').send_keys("Romina")
        self.driver.find_element_by_id('lastName').send_keys("Milillo")

        tipoDni = Select(self.driver.find_element_by_id('id_type'))
        tipoDni.select_by_value("DNI")

        self.driver.find_element_by_id('id_value').send_keys("34503338")

        diaNacimiento = Select(self.driver.find_element_by_id('day_select'))
        diaNacimiento.select_by_value("28")

        mes = Select(self.driver.find_element_by_id('month_select'))
        mes.select_by_visible_text("Marzo")

        anioNacimiento = Select(self.driver.find_element_by_id('year_select'))
        anioNacimiento.select_by_value("1950")

        generoMasculino = self.driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/section[3]/div/form/fieldset[1]/div[2]/div[3]/div/div/div/div[1]/label')
        generoMasculino.click()
        
        self.driver.find_element_by_id('codphone').send_keys("11")
        self.driver.find_element_by_id('phone').send_keys("1566778899")
        self.driver.find_element_by_id('email').send_keys("joseperez@gmail.com")
        self.driver.find_element_by_id('street_name').send_keys("Laprida")
        self.driver.find_element_by_id('street_number').send_keys("2020")
        self.driver.find_element_by_id('floor').send_keys("4")
        self.driver.find_element_by_id('room').send_keys("2")
        self.driver.find_element_by_id('zip_code').send_keys("1888")
      
        terminos = self.driver.find_element_by_id('terms-conditions')        
        terminos.click()

    def irPaso4(self):
        continuar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar))
        continuar.click()



