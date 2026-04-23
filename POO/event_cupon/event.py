class Event:
    def __init__(self, id, titulo, descricao, data, local, preco, id_usuario, nome_criador=None, is_admin=False):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.local = local
        self.preco = preco
        self.id_usuario = id_usuario
        self.nome_criador = nome_criador
        self.is_admin = is_admin

    def __repr__(self):
        tipo_criador = "Admin" if self.is_admin else "Usuário"
        return (
            f"id: {self.id}\n"
            f" titulo: {self.titulo}\n"
            f" descricao: {self.descricao}\n"
            f" data: {self.data}\n"
            f" local: {self.local}\n"
            f" preco: R${self.preco:.2f}\n"
            f" criado por: {self.nome_criador} ({tipo_criador})"
        )