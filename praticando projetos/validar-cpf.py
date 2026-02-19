# Programa pra validar CPF.

def validar_cpf(cpf):
    if not cpf.isdigit(): #isdigit para garantir que não há letras ou caracteres.
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11: #len != 11 - verificar quantidade de letras.
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."
 
cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))