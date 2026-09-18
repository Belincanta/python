from rich import print, inspect
from class005 import Pessoa, Aluno, Professor, Funcionario

a1 = Aluno(nome="Alessandro", idade=30, curso="Matemática", turma="A005")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Olavo", 47, "Educação fisica", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Ingrid", 45, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)