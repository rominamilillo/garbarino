from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.autocomplete = (By.ID, 'autocomplete-input')
        self.boton = (By.XPATH, '//*[@id="autocomplete-element"]/button')
        self.driver = driver

    def ingresar_busqueda(self, bla):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.autocomplete)).send_keys(bla)

    def buscar(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.boton)).click()

