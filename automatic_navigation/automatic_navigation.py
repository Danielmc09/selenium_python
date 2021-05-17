import unittest
from selenium import webdriver
#libreria para el tiempo de ejecución entre acciones
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://google.com/")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('platzi')
        search_field.submit()

        #retroceder en el navegador
        driver.back()
        sleep(3)
        #avanzar en el navegador
        driver.forward()
        sleep(3)
        #refrescar el navegador
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)