import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

""" 
Cambiat self por cls con el decorador @classmethod nos ayuda
ha abrir las pruebas en el mismo navegador
"""


#Clase para la prueba que extiende de unnitest.TestCase
#se divide en este caso en 3 componente pero pueden ser más
class HelloWorld(unittest.TestCase):

    #Setup va a ejecutar todo lo necesario antes de 
    #hacer una prueba, prepara el entorno de la prueba
    @classmethod
    def setUp(cls):
        #chromedriver se descarga del navegador
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = cls.driver
        #le decimos a el navegador que espere 10 segundos
        driver.implicitly_wait(10)

    #Este es nuestro caso de prueba donde vamos a realizar
    #una serie de opciones para que el navegador las automatice
    def test_hello_world(cls):
        driver = cls.driver
        #le damos la direccion para ejecutar
        driver.get('https://emprendedoras.elearning.bavaria.co/')

    def test_visit_platzi(cls):
        cls.driver.get('https://www.platzi.com')

        

    #Despues van a ocurrir otras acciones para finalizar
    #Generalmente es cerrar el navegador despues de hacer las pruebas
    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'hello_world_report'))