class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
    
    def mostrarplaca(self):
        print('A placa do veículo é', self.placa)

c1 = Carro("Jeep", "MBO1776", 2012)

c1.mostrarplaca()