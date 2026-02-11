macas = int(input("Digite a quantidade de maçãs vendidas:"))
banana = int(input("Digite a quantidade de bananas vendidas:"))

if macas > banana:
    print("As maças tiveram mais vendas.")
elif banana > macas:
    print("As bananas tiverem mais vendas.")
else:
    print("As vendas foram iguais.")