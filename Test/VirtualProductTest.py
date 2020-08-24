from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Pages.DetailPage import DetailPage
from Pages.CartPage import CartPage
from Pages.Paso1Page import Paso1Page
from Pages.Paso2Page import Paso2Page
from Pages.Paso3Page import Paso3Page
from Pages.Paso4Page import Paso4Page

import random
import unittest
import requests



def  obtener_producto_virtual(url, headers):
    productos = (requests.get(url, headers=headers)).json()
    ran = random.randint(0, int(productos['size'])-1)
    return productos['items'][ran]

class Garbarino(unittest.TestCase):

    def setUp(self):
        url = "http://api-support-prod.garba.ninja/repositories/garbarino/virtual"
        headers = {
            'Content-Type': 'application/json',
            'api-key': '79b36129-cdd0-4034-8da7-ed94223c02a1'
        }
        base_URL = "https://www.garbarino.com"

        self.driver = webdriver.Chrome('chromedriver')
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        url_producto = base_URL + "/producto/" + obtener_producto_virtual(url, headers)
        self.driver.get(url_producto)
        self.DetailPage = DetailPage(self.driver)
        self.CartPage = CartPage(self.driver)
        self.Paso1Page = Paso1Page(self.driver)
        self.Paso2Page = Paso2Page(self.driver)
        self.Paso3Page = Paso3Page(self.driver)
        self.Paso4Page = Paso4Page(self.driver)


    def test_checkout(self):
        self.DetailPage.ir_a_carrito()
        self.driver.implicitly_wait(15)

        self.CartPage.setear_cantidad_2()
        self.CartPage.ir_a_checkout()

        self.Paso1Page.irPaso2Virtual()
        self.driver.implicitly_wait(15)

        self.Paso2Page.seleccionarPrimerTarjeta()
        self.Paso2Page.seleccionarCuota()
        self.Paso2Page.irPaso3()

        self.Paso3Page.completarPaso3()
        self.Paso3Page.irPaso4()


if __name__ == "__main__":
    unittest.main()