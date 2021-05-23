import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    #lista para indicar el número de filas que contiene
    rows = []
    #abrimos el archivo csv en modo lectura
    data_field = open(file_name, 'r')
    reader = csv.reader(data_field)
    #omitimos el header o cabecera
    next(reader, None)

    #recorrecmos los datos y los agregamos a la lista vacia
    for row in reader:
        rows.append(row)
    return rows 

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    #Contiene la cantidad de datos que vamos a buscar en la tupla
    #para pasarselos a la función con la cantidad de datos
    @data(*get_data('testdata.csv'))
    #decorador para desempaquetar las tuplas y se puedan usar de forma 
    #individual
    @unpack

    # search_value : valor de la busqueda
    # expected_count : cantidad de resultados que esperamos encontrar 
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0 :
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_elements_by_tag_name('note-msg')
            self.assertEqual('You search returns no results.', message)

        print(f'found {len(products)} products')
       
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)