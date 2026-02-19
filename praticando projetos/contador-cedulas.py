def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input("Digite o valor do saque: R$ "))

        if valor <= 0:
            print("O valor deve ser positivo.")
            return

        if valor % 2 != 0:
            print("Valor inválido. O caixa não possui cédulas de R$ 1.")
            return

    except ValueError:
        print("Erro: Digite um valor numérico válido.")
        return

    print("\nCédulas entregues:")

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            print(f"{quantidade} cédula(s) de R$ {cedula}")
            valor %= cedula

caixa_eletronico()
