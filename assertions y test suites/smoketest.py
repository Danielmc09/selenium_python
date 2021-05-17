from unittest import TestLoader, TestSuite
#para generar el reporte
from pyunitreport import HTMLTestRunner
#Importa la clase de los otros archivos
from assertions import AssertionsTest
from searchtest import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)
#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_test])
#para generar los reporters
kwargs = {
    'output': 'smoke-report'
}
#la variable runner almacena un reporte generado por HTMLTestRuner
#usa como argumento "kwargs"
runner = HTMLTestRunner(**kwargs)
#corro el rurner con la suite de prueba
runner.run(smoke_test)