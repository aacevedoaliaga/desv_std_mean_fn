import unittest
from src.desv_std_mean_fn.DStandarMean import DStandarMean

class Prueba_media(unittest.TestCase):
    def test_media(self):

        #Arrange
        media = DStandarMean()
        data=[15.82, 15.23]
        resultadoesperado= 16.525, 0.00

        #Do
        resultadoActual = DStandarMean.DStandar_Mean(self, data)


        #Assert
        self.assertEqual(resultadoesperado, resultadoActual)


