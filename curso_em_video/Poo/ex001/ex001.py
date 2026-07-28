#declaração da classe - serve para criar um modelo para ser instancida depois
class Gafanhoto: 
    def __init__(self): #método construtor
        #atributos de instância
        self.nome = ""
        self.idade = 0 

    #declaração de métodos
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e possui {self.idade} anos de idade."

#declaração do objeto - serve para instanciar a classe

#g1 é o objeto que se refere ao self, que por sua vez é um nome genérico de um atributo de instância, sendo substituido pelo objeto.
g1 = Gafanhoto() #para chamar a classe
g1.nome = "Alessandro" #para passar o atributo
g1.idade = 29 #para passar o atributo
g1.aniversario() #para chamar a função 
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Hellen"
g2.idade = 28
print(g2.mensagem())
