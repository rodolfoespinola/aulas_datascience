class Pessoa:
    def __init__(self, nome, idade, altura): 
        self.__nome = nome  # Adiciona proteção
        self.__idade = idade  
        self.altura = altura  
        
    def apresentar(self):
        print("Olá, meu nome é:",self.__nome, ", tenho", self.__idade, ' anos e tenho', self.altura, ' de altura')

    def get_nome(self):
        return self.__nome
    
    def set_idade(self,nova_idade):
        if nova_idade < 40:
            self.__idade = nova_idade

p1 = Pessoa("João", 33, "1,80")
p2 = Pessoa("Karina", 28, "1,70")

p1.apresentar()
p2.apresentar()

p1.set_idade(35)
p1.apresentar()

print(p1.get_nome())

