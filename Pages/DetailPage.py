from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pdb

class DetailPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.comprar = (By.ID, "purchaseButton")

    def ir_a_carrito(self):
        comprar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.comprar))
        ActionChains(self.driver).move_to_element(comprar).click(comprar).perform()



