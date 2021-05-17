import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LenguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_lenguage(self):
        exp_option = ['English', 'French', 'German']
        act_option = []

        select_lenguage = Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3, len(select_lenguage.options))

        #recorremos las opciones que contiene el id
        #agregamos el resultado de el for en la lista vacia
        for option in select_lenguage.options:
            act_option.append(option.text)

        #validamos que sean iguales las dos listas
        self.assertListEqual(exp_option, act_option)

        #validamos que el primer campo es english
        self.assertEqual('English', select_lenguage.first_selected_option.text)

        #seleccionesmos el lenguaje German
        select_lenguage.select_by_visible_text('German')
        #Validamos que la url si sea la correcta cuando se selecciona aleman
        self.assertTrue('store=german' in self.driver.current_url)
        
        
        select_lenguage = Select(self.driver.find_element_by_id('select-language'))
        #tambien podemos selecciona un lenguaje por su id en este caso english
        select_lenguage.select_by_index(0)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)