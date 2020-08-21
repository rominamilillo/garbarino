from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pdb

class CartPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.seleccion = (By.XPATH, '//*[contains(@id, "idQuantity")]')
        self.continuar = (By.ID, 'cart-buy-btn')

    def setear_cantidad_2(self):
        setear_cantidad = Select(self.driver.find_element(*self.seleccion))
        setear_cantidad.select_by_index(1)

    def ir_a_checkout(self):
        continuar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.continuar))
        continuar.click()
        self.driver.implicitly_wait(3)

