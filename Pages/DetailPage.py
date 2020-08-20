from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pdb

class DetailPage(object):
    def __init__(self, driver):
        self.driver = driver
        #self.comprar = (By.XPATH, '//*[@id="purchaseButton"]')
        self.comprar = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/div[3]/button')

    def ir_a_carrito(self):
        comprar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.comprar))
        ActionChains(self.driver).move_to_element(comprar).click(comprar).perform()
        #comprar.click()



