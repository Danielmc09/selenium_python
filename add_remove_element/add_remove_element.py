import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_partial_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('Cuantos elementos quieres agregar?:'))
        elements_remove = int(input('Cuantos elementos quieres borrar?:'))
        total_elements = elements_added - elements_remove

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('estas intentando eliminar más botones de los que existen')
                break

        if total_elements > 0:
            print(f'los elementos totales que quedaron son {total_elements}')
        else:
            print('0 elementos')

        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)