from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
from selenium.webdriver import ActionChains
import time

class Paso1Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.ciudad = (By.ID, 'c1ty')
        self.selectCity = (By.XPATH, '//*[@id="remote"]/div/div/div[1]')
        self.pickup = (By.XPATH, "//*[@id='checkout-entrega']//label")

        self.sucursal = (By.XPATH, '/html/body/main/div/div[1]/section[1]/div[3]/form[1]/div[2]/div[1]/ul/li[1]/ul/li[2]/label/input')
        
        self.continuar = (By.ID, "continue-pickup")

    def ingresarCiudad(self, city): 
        ciudad = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.ciudad))
        ActionChains(self.driver).move_to_element(ciudad).send_keys(city).perform()
        seleccionar = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.selectCity))            
        seleccionar.click()
        self.driver.implicitly_wait(15)

    def seleccionarCiudad(self):
        pickup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.pickup))
        pickup.click()
        time.sleep(2)
        sucursal = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.sucursal))
        ActionChains(self.driver).move_to_element(sucursal).perform()
        sucursal.click()

    def irPaso2(self):
        continuar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar))
        continuar.click()
        self.driver.implicitly_wait(15)


