from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ListPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.ordenar = (By.ID, 'sorter')
        self.ascendente = (By.ID, 'price_desc')
        self.paginado = (By.XPATH, '//li[contains(@class, "pagination__page")]/a')
        self.precio_minimo = (By.ID, 'amount-min')
        self.precio_maximo = (By.ID, 'amount-max')
        self.precio_setear = (By.ID, 'prange')
        self.producto = (By.XPATH, "//*[contains(@id, 'item-description')]")

    def orden(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.ordenar)).click()

    def ordenar_asc(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.ascendente)).click()

    def setearMaximo(self, maximo):
        precio_maximo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.precio_maximo))
        precio_maximo.clear()
        precio_maximo.send_keys(maximo)

    def setearMinimo(self, minimo):
        precio_minimo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.precio_minimo))
        precio_minimo.clear()
        precio_minimo.send_keys(minimo)

    def filtrar_precio(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.precio_setear)).click()
        self.driver.implicitly_wait(3)

    def paginar(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.paginado)).click()
      
    def ir_a_primer_producto(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.producto)).click()
        #self.driver.implicitly_wait(3)
