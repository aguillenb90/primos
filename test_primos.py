
import unittest
from primos import primos_hasta_100

class TestPrimosHasta100(unittest.TestCase):

    def test_cantidad_primos(self):
        resultado = primos_hasta_100()
        self.assertEqual(len(resultado), 25)  # Hay 25 números primos entre 0 y 100

    def test_ultimo_primo(self):
        resultado = primos_hasta_100()
        self.assertEqual(resultado[-1], 97)  # El último primo menor o igual a 100 es 97

if __name__ == '__main__':
    unittest.main()
