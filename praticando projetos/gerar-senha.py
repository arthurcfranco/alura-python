import random
 
def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
 
    senha = [
        # Utilizar random.choice() para selecionar uma letra maiúscula, uma letra minúscula, um número e um caractere especial.
        random.choice(maiusculas), 
        random.choice(minusculas),
        random.choice(numeros),     
        random.choice(especiais)    
    ]
 
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8)) # Utilizar random.choices(todos_caracteres, k=8) para adicionar 8 caracteres aleatórios à senha
    random.shuffle(senha) # Utilizar random.shuffle(senha) para reorganizar os caracteres da lista
    return ''.join(senha)
 
print(f"Senha gerada: {gerar_senha()}")