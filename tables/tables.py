import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_partial_link_text('Sortable Data Table').click()

    def test_sort_table(self):
        driver = self.driver
        column_title = 5
        row_data = 4

        table_data = [[] for i in range(column_title)]
        print(table_data)

        for i in range(column_title):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(row_data):
                row_dataa = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{j + 1}]')
                table_data[i].append(row_dataa.text)

        print(table_data)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)