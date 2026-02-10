class Pessoa:
    def __init__(self, nome, idade, altura): # Função construtora. Entre parênteses, os atributos.
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade
        self.altura = altura  # Atributo altura
        
    def apresentar(self):
        print("Olá, meu nome é:",self.nome, ", tenho", self.idade, ' anos e tenho', self.altura, ' de altura')

p1 = Pessoa("João", 33, "1,80")
p2 = Pessoa("Karina", 28, "1,70")

p1.apresentar()
p2.apresentar()

print(p1.nome)