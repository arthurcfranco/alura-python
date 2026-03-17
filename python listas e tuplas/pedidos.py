pedidos = input("Pedidos feitos (separados por vírgula): ").split(", ")
pedidos.pop() # Para remover o ultimo item da lista
print("Pedidos finais:")
print(pedidos)