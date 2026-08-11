from rich import print

class Funcionario:
    """
        Permite que o funcionário se apresente
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print(f"Olá, eu sou [green]{self.nome}[/] trabalho no setor {self.setor} no cargo de {self.cargo}, na empresa Curso em Video!")

#declaração do objeto
fun1 = Funcionario(nome="Alessandro", setor="Processos", cargo="Assessor")



