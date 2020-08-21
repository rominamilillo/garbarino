import unittest
from selenium import webdriver
import pdb
from Pages.HomePage import HomePage
from Pages.ListPage import ListPage
from Pages.DetailPage import DetailPage
from Pages.CartPage import CartPage
from Pages.Paso1Page import Paso1Page
from Pages.Paso2Page import Paso2Page
from Pages.Paso3Page import Paso3Page
from Pages.Paso4Page import Paso4Page

class Garbarino(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('https://www.garbarino.com/')
        self.HomePage = HomePage(self.driver)
        self.ListPage = ListPage(self.driver)
        self.DetailPage = DetailPage(self.driver)
        self.CartPage = CartPage(self.driver)
        self.Paso1Page = Paso1Page(self.driver)
        self.Paso2Page = Paso2Page(self.driver)
        self.Paso3Page = Paso3Page(self.driver)
        self.Paso4Page = Paso4Page(self.driver)

    def testBusqueda_y_checkout(self):
        self.HomePage.ingresar_busqueda('cocina')
        self.ListPage.ordenar_asc()
        self.ListPage.filtrar_precio("100", "500000")
        self.ListPage.paginar()
        self.ListPage.ir_a_primer_producto()
        self.driver.implicitly_wait(3)
        self.DetailPage.ir_a_carrito()
        self.driver.implicitly_wait(15)
        self.CartPage.setear_cantidad_2()
        self.CartPage.ir_a_checkout()
        self.Paso1Page.ingresarCiudad("caba")
        self.Paso1Page.seleccionarCiudad()
        self.Paso1Page.irPaso2()
        self.Paso2Page.seleccionarPrimerTarjeta()
        self.Paso2Page.seleccionarCuota()   
        self.Paso2Page.irPaso3()
        self.Paso3Page.completarPaso3()
        self.Paso3Page.irPaso4()
        #breakpoint()   

if __name__ == "__main__":
    unittest.main()





