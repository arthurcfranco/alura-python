# Programa para calcular gorjeta

# Entrada de dados
valor_conta = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem de gorjeta (%): "))

# Cálculo da gorjeta
valor_gorjeta = valor_conta * (porcentagem / 100)

# Cálculo do total
total = valor_conta + valor_gorjeta

# Saída de dados
print(f"\nValor da gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")