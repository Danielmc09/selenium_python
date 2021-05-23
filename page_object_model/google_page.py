from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Separamos cada una de las acciones a realizar esto con el fin
de que sea mucho más abstracto las pruebas
"""


class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.google.com'
        self.search_locator = 'q'

    #verificamos que el sitio web cargue correctamente
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_all_element_located((By.NAME, 'q')))
        return True

    #ubicamos el campo donde ponemos los terminos
    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        #retornamos el atributo de input_field el valor
        return input_field.get_attribute('value')

    #metodo para ingresar a la url 
    def open(self):
        self._driver.get(self._url)

    #input_field : ubicamos la barra de busqueda
    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        #enviamos la simulacion de las teclas con el keyword
        input_field.send_keys(keyword)

    #metodo para hacer el envio del termino de busqueda
    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()

    #llamamos el metodo type_search para enviarlo
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()
