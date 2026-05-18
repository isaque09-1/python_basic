class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        print(f"Livro: {self.titulo}")
        print("-" * 40)
        print(f"Autor: {self.autor.nome} ({self.autor.nacionalidade})")
        print("-" * 40)


if __name__ == "__main__":
    autor = Autor("Machado de Assis", "Brasileiro")
    livro = Livro("Dom Casmurro", autor)
    livro.exibir_info()



class Processador :
    def __init__(self , modelo ):
        self.modelo = modelo



class MemoriaRAM :
    def __init__(self, capacidade_gb):
        self.capacidade_gb = capacidade_gb



class Computador :
    def __init__(self, processador , memoria_ram):
        self.processador = processador
        self.memoria_ram = memoria_ram


    def status(self):
        print (f"PROCESSADOR : {self.processador.modelo}")
        print("-" * 40 )
        print(f"MEMORIA RAM : {self.memoria_ram.capacidade_gb}")
        print("-" * 40 )


cpu = Processador("Ryzen 5 5600GT")
ram = MemoriaRAM(64)

pc = Computador(cpu , ram)

pc.status()
    


class Musica:
    def __init__(self, nome, artista):
        self.nome = nome
        self.artista = artista

    def __str__(self):
        return f"{self.nome} - {self.artista}"

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def add_music(self, musica: Musica):
        self.musicas.append(musica)
        print(f"Música '{musica}' adicionada à playlist '{self.nome}'.")

    def play_all_music(self):
        print(f"\nTocando playlist '{self.nome}':")
        print("-" * 40)
        for musica in self.musicas:
            print(musica)
        print("=" * 40)

m1 = Musica("Bohemian Rhapsody", "Queen")
playlist = Playlist("Minhas Favoritas")
playlist.add_music(m1)
playlist.play_all_music()