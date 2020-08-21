from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class Paso1Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.ciudad = (By.ID, 'c1ty')
        self.pickup = (By.XPATH, '//p[contains(text(), "Retiro en sucursal ")]')
        self.sucursal = (By.XPATH, '//*[@id="stores"]//label')
        self.continuar = (By.ID, "continue-pickup")

    def ingresarCiudad(self, city): 
        ciudad = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.ciudad))            
        ciudad.send_keys(city)
        time.sleep(3)
        ciudad.send_keys(Keys.ENTER)

    def seleccionarSucursal(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.pickup)).click()
        sucursal = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.sucursal))
        ActionChains(self.driver).move_to_element(sucursal).click(sucursal).perform()

    def irPaso2(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar)).click()
        self.driver.implicitly_wait(15)


