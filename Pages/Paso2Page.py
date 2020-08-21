from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
from selenium.webdriver import ActionChains
import time

class Paso2Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.financiacion = (By.NAME, 'financiacion')
        self.cuotas = (By.XPATH, "//select[@name='finance_quota']/option[2]")
        self.continuar = (By.ID, 'continue')

    def seleccionarPrimerTarjeta(self): 
        financiacion = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.financiacion))
        ActionChains(self.driver).move_to_element(financiacion).click(financiacion).perform()

    def seleccionarCuota(self):
        cuotas = self.driver.find_element(*self.cuotas)
        time.sleep(1)
        cuotas.click()


    def irPaso3(self):
        continuar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar))
        continuar.click()


