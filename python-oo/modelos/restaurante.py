class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante ()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

restaurante_pizza = Restaurante ()
restaurante_pizza.nome = 'Giuseppe'
restaurante_pizza.categoria = 'Rodizio'
if restaurante_pizza.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')
if restaurante_pizza.categoria == 'Rodizio':
    print('A categoria é rodizio.')
else:
    print('A categoria não é rodizio.')

restaurante_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')