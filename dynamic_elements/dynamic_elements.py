import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_partial_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < menu:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{ i + 1 }]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'La opción no ha sido encontrada { i + 1}')
                    tries += 1 
                    driver.refresh()
        
        print(f'finalizado en {tries} intentos ')


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)