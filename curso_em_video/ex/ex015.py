# cores no terminal
nome = "Alessandro"
print(f"Olá mundo, eu sou o {"\33[4;31m"} {nome} {"\33[m"}!!!")

# código base para inserir uma cor \33[m  - antes do m é necessário colocar as configurações de style, text e background.
# quando você consigura a cor antes do texto, você pode fechar para não impactar a cor de todo o texto usando o \33[m
