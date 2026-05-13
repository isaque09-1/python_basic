class Autor :
    def __init__(self , nome , nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro :
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def exibir_info(self):
        print(f"Livro : {self.titulo}")
        print(f"Autor : {self.autor.nome}")


a1 = Autor("Machado de Assis", "Brasileiro")
l1 = Livro("Dom Casmurro", a1)

l1.exibir_info()



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
        print(f"MEMORIA RAM : {self.memoria_ram.capacidade_gb}")


cpu = Processador("Ryzen 5 5600GT")
ram = MemoriaRAM(64)

pc = Computador(cpu , ram)

pc.status()
    


class Musica :
    def __init__ (self, nome , artista):
        self.nome = nome 
        self.artista = artista

    def __str__(self):
        return f"{self.nome} - {self.artista}"
    

class Playlist :
    def __init__(self,nome):
        self.nome = nome 
        self.musica = []


    def add_music(self, musica:Musica):
        self.musica.append(musica)
        print(f"Musica : {self.musica} adicionada a playlist {self.nome}.")
