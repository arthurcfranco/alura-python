notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ") #  split(", ") divide a string de entrada das notas dos alunos em uma lista de notas.
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas) # sum calcular soma de todas as notas, len para determinar o total de elementos.
print(f"Média final da turma: {media:.2f}")