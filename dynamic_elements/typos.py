import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver

        #seleccionamos el elemento por su selector
        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        #Capturamos el texto del elemento
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        #Recorremos el valor obtenido en la variable hasta que sea correcto
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            driver.refresh()
        
        #Recorremos found hasta el momento en el que el texto obtenido en el
        #objeto sea igual a el que tenemos como string para comparar
        #y cambiamos el valor de la variable found a True cuando esto sucede
        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True
        
        #Validamos que el valor de found ya sea True
        self.assertEqual(found, True)

        print(f'a selenium le costo {tries} intentos')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)