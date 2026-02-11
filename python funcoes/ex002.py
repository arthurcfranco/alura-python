def saudacao(hora):
    if hora < 12:
        return "bom dia!"
    elif hora < 18:
        return 'boa tarde'
    else:
        return 'boa noite'

hora_atual = int(input("Digite a hora atual (0-23): ")) 
print(saudacao(hora_atual)) 