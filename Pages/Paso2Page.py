from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb
from selenium.webdriver import ActionChains

class Paso2Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.financiacion = (By.NAME, 'financiacion')
        self.cuotas = (By.XPATH, '/html/body/main/div/div[1]/section[2]/div/form/fieldset[3]/div/div[1]/select')

    def primerTarjeta(self): 
        financiacion = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.financiacion))
        ActionChains(self.driver).move_to_element(financiacion).click(financiacion).perform()

    #def seleccionarCuota(self):
        #breakpoint()
        #cuotas = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.cuotas))
        #ActionChains(self.driver).move_to_element(cuotas).perform()
        #cuotas.select_by_index(1)






