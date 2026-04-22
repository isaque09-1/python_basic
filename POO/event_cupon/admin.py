from user import User
from db import USUARIOS, EVENTOS, CUPONS
from event import Event
from cupon import Cupom

class Admin(User):
    def __init__(self, id, nome, senha, email):
        super().__init__(id, nome, senha, email)
        self.is_admin = True

    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f" nome: {self.nome}\n"
            f" email: {self.email}\n"
            f" is_admin: {self.is_admin}"
        )

    @classmethod
    def criar_usuario(cls, nome, senha, email):
        usuario = User(len(USUARIOS) + 1, nome, senha, email)
        usuario.adicionar()
        return usuario

    @classmethod
    def criar_admin(cls, nome, senha, email):
        admin = Admin(len(USUARIOS) + 1, nome, senha, email)
        admin.adicionar()
        return admin

    @classmethod
    def listar_usuarios(cls):
        return USUARIOS

    @classmethod
    def deletar_usuario(cls, id):
        for usuario in USUARIOS:
            if usuario.id == id:
                USUARIOS.remove(usuario)
                print(f"Usuário '{usuario.nome}' deletado!")
                return
        print("Usuário não encontrado!")

    def criar_evento(self, titulo, descricao, data, local, preco):
        evento = Event(len(EVENTOS) + 1, titulo, descricao, data, local, preco, self.id, self.nome, True)
        EVENTOS.append(evento)
        print(f"Evento '{titulo}' criado pelo admin {self.nome}!")
        return evento

    def deletar_evento(self, id_evento):
        for evento in EVENTOS:
            if evento.id == id_evento:
                EVENTOS.remove(evento)
                print(f"Evento '{evento.titulo}' deletado pelo admin {self.nome}!")
                return
        print("Evento não encontrado!")

    def criar_cupom(self, titulo, desconto, validade, id_evento):
        for evento in EVENTOS:
            if evento.id == id_evento:
                cupom = Cupom(len(CUPONS) + 1, titulo, desconto, validade, id_evento)
                CUPONS.append(cupom)
                print(f"Cupom '{titulo}' criado pelo admin {self.nome}!")
                return cupom
        print("Evento não encontrado!")

    def deletar_cupom(self, id_cupom):
        for cupom in CUPONS:
            if cupom.id == id_cupom:
                CUPONS.remove(cupom)
                print(f"Cupom '{cupom.titulo}' deletado pelo admin {self.nome}!")
                return
        print("Cupom não encontrado!")

    @classmethod
    def listar_eventos(cls):
        return EVENTOS

    @classmethod
    def listar_cupons(cls):
        return CUPONS