import unittest
from src.desv_std_mean_fn.DStandarMean import DStandarMean

class Prueba_media(unittest.TestCase):
    def test_media(self):

        #Arrange
        media = DStandarMean()
        data=[15.62, 15.90]
        resultadoesperado= 15.760, 0.140

        #Do
        resultadoActual = DStandarMean.DStandar_Mean(self, data)


        #Assert
        self.assertEqual(resultadoesperado, resultadoActual)


