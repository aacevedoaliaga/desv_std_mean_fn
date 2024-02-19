class DStandarMean:
    # TODO
    # TODO
    # TODO
    def DStandar_Mean(self, data):
        mean = sum(data) / len(data)
        squared_diff = [(x - mean) ** 2 for x in data]
        variance = sum(squared_diff) / len(data)
        std_dev = variance ** 0.5
        return mean, std_dev

    # if __name__ == '__main__':
    #input_data = input("Ingresa los datos separados por espacios: ")
    #try:
    #    data = [float(x) for x in input_data.split()]
    #    media, desv = DStandar_Mean(data)
    #    print("La Media es:", media)
    #    print("La Desviación Estándar es:", desv)
    #except ValueError:
    #    print("Ingrese datos numéricos válidos por favor")
