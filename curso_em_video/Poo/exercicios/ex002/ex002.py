#declaração da classe - serve para criar um modelo para ser instancida depois
class Gafanhoto: 
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma pessoa, use:
    variavel: Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): #método construtor
        #atributos de instância
        self.nome = nome
        self.idade = idade

    #declaração de métodos
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e possui {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e possui {self.idade} anos de idade."

#declaração do objeto - serve para instanciar a classe

#g1 é o objeto que se refere ao self, que por sua vez é um nome genérico de um atributo de instância, sendo substituido pelo objeto.
g1 = Gafanhoto("Alessandro", 29) #para chamar a classe
g1.aniversario() #para chamar a função 
print(g1.mensagem())

print(g1) #substitui o print(g1.mensagem()), devido o construtor

#g2 = Gafanhoto("Hellen", "28")
#print(g2.mensagem())

#g3 = Gafanhoto()
#print(g3.mensagem())

#print(g1.__doc__) #para guspir a doc string
