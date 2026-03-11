voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou sair para encerrar): ")
    if nome == "sair":
        break
    voluntarios.append(nome)

print(voluntarios)