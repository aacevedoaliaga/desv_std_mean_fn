import unittest
from src.desv_std_mean_fn.DStandarMean import DStandarMean
class Prueba_media(unittest.TestCase):
    def setUp(self):
        self.ds_media = DStandarMean()
    def tearDown(self):
        self.ds_media = None

    def test_float_str(self):
        data = [15.62, 15.90]
        resultadoActual = self.ds_media.DStandar_Mean(data)
        resultadoesperado = (15.760, 0.140)
        self.assertEqual(resultadoesperado, resultadoActual)





