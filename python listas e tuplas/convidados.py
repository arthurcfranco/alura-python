convidados = ["Ana", "Carlos", "João"]

print("Lista inicial de convidados:")
print(convidados)

novo_nome = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição onde deseja inserir: "))

convidados.insert(posicao, novo_nome)

print("\nLista atualizada:")
print(convidados)