primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3
print(f"A média do aluno é: {media:.2f}")

if media >= 7:
    print('Aprovado')
elif 5<= media < 7:
    print('Recuperação')
else:
    print('Reprovado')