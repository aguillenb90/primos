import unittest
import numpy as np
from calculoCirculo import area_circulo  # Asegúrate de importar tu función

class TestAreaCirculo(unittest.TestCase):
    
    def test_area_circulo_entero(self):
        """Test con radio entero"""
        self.assertAlmostEqual(area_circulo(1), 3.141592653589793, places=6)
        self.assertAlmostEqual(area_circulo(5), 78.53981633974483, places=6)
    
    def test_area_circulo_float(self):
        """Test con radio float"""
        self.assertAlmostEqual(area_circulo(2.5), 19.634954084936208, places=6)
    
    def test_area_circulo_array(self):
        """Test con array de radios"""
        radios = np.array([1, 2, 3])
        resultados_esperados = np.array([3.14159265, 12.56637061, 28.27433388])
        np.testing.assert_array_almost_equal(
            area_circulo(radios),
            resultados_esperados,
            decimal=6
        )
    
    
if __name__ == '__main__':
    unittest.main()