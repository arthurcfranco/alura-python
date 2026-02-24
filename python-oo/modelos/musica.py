class Musica:
    musicas = []

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.artista}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica_mpb} | {musica_rock}')


musica_mpb = Musica (nome='Dom Quixote', artista='Humberto Guessinger', duracao=300)
musica_rock = Musica (nome='Chop Suey!', artista='System of a down', duracao=430)

Musica.listar_musicas()
