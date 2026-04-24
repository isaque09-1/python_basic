class Event:
    def __init__(self, id, titulo, descricao, data, local, preco, id_usuario, nome_criador=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.local = local
        self.preco = preco
        self.id_usuario = id_usuario
        self.nome_criador = nome_criador

    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f" titulo: {self.titulo}\n"
            f" descricao: {self.descricao}\n"
            f" data: {self.data}\n"
            f" local: {self.local}\n"
            f" preco: R${self.preco}\n"
            f" criado por: {self.nome_criador}"
        )

        