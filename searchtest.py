import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        #esperar 15 segundos antes de ejecutar la prueba
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        #indicamos que se buscara por id del elemento
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        #indicamos que se buscara por name del elemento
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self):
        #indicamos que se buscara por la clase del elemento
        searc_field = self.driver.find_element_by_class_name('input-text')
    
    def test_search_text_field_by_button(self):
        button = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        #indicamos que se buscara por la clase del elemento
        banner_list = self.driver.find_element_by_class_name('promos')
        #almacenaremos la busqueda de esos banners los buscara por su etiqueta html
        banners = banner_list.find_elements_by_tag_name('img')
        #verificamos que sean 3 imagenes de acuerdo a la variable banners
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        #acceder a el elementopor el xpath
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img')

    def test_shopping_cart(self):
        #accedemos a el elemento por css
        shopping_cart_icon = self.driver.find_elements_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'searchtest'))