from rich import print
from rich import inspect

class Funcionario:
    """
        Permite que o funcionário se apresente
    """
    #atributo de classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f"Olá, eu sou [green]{self.nome}[/] trabalho no setor {self.setor} no cargo de {self.cargo}, na empresa {Funcionario.empresa}!"

#declaração do objeto
fun1 = Funcionario(nome="Alessandro", setor="Processos", cargo="Assessor")
#inspect(fun1)
print(fun1.apresentação())



