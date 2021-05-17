import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_partial_link_text('Dynamic Controls').click()

    def test_dynamic_control(self):
        driver = self.driver

        #Buscamos el selector de CSS del campo checkbox para habilitarlo
        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()

        #Con el selector seleccionamos el campo del boton para remover el checkbox
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()

        #Esperamos 15 segundos a que el campo este habilitado nuevamente para clickearlo de nuevo
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()

        #Activamos el campo de texto con el selector del boton
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()

        #Esperamos 15 segundos mientras habilita el campo
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        #Seleccionamos el campo y le enviamos la palabra Platzi
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        #Clickeamos nuevamente el boton de desactivar
        enable_disable_button.click()


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)