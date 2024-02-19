import unittest
from src.desv_std_mean_fn.DStandarMean import DStandarMean
class Prueba_media(unittest.TestCase):
    def setUp(self):
        self.ds_media = DStandarMean()
    def tearDown(self):
        self.ds_media = None

    def test_float(self):
        data = [15.62, 15.90]
        resultadoActual = self.ds_media.DStandar_Mean(data)
        resultadoesperado = (15.760, 0.140)
        self.assertEqual(resultadoesperado, resultadoActual)

    def test_negativo(self):
        data = [15.00,16.06,15.14,-20.00,17.25,14.37,14.28 ]
        resultadoActual = self.ds_media.DStandar_Mean(data)
        resultadoesperado = (10.300,12.407)
        self.assertEqual(resultadoesperado, resultadoActual)

    def test_integer_str(self):
        data = [15.00, 16.06, 15.14, -20.00, 17.25, 14.37, 14.28]
        data_with_str = ["a", 16.06, 15.14, -20.00, 17.25, 14.37, 14.28]
        self.assertListEqual(data, data_with_str)
        with self.assertRaises(ValueError):
            self.ds_media.DStandar_Mean(data_with_str)




