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

class Aluno(Pessoa):
    def __init__(self,nome,idade,altura,matricula):
        super().__init__(nome,idade,altura) #Acessa a classe mãe
        self.matricula = matricula
    def estudante(self):
        print('A matrícula do aluno é',self.matricula)
    def apresentar(self):
        print("Olá, meu nome é:",super().get_nome(), " e minha matrícula é",self.matricula) # A forma de apresentar é diferente da pessoa

aluno1 = Aluno('Pedro',30,'1,90','0006780')

aluno1.estudante()
aluno1.apresentar()


