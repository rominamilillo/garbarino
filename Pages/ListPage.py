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
        ordenar = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.ordenar))
        ordenar.click()

    def ordenar_asc(self):
        ascendente = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ascendente))
        ascendente.click()

    def filtrar_precio(self, minimo, maximo):
        precio_minimo = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.precio_minimo))
        precio_maximo = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.precio_maximo))
        precio_setear = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.precio_setear))
        precio_minimo.clear()
        precio_minimo.send_keys(minimo)
        precio_maximo.clear()
        precio_maximo.send_keys(maximo)
        precio_setear.click()
        self.driver.implicitly_wait(3)

    def paginar(self):
        paginado = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.paginado))
        paginado.click()
      
    def ir_a_primer_producto(self):
        producto = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.producto))
        producto.click()
        self.driver.implicitly_wait(3)

