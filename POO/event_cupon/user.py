from db import USUARIOS, EVENTOS, CUPONS
from event import Event
from cupon import Cupom

class User:
    def __init__(self, id, nome, senha, email):
        self.id    = id
        self.nome  = nome
        self.senha = senha
        self.email = email

    def adicionar(self):
        USUARIOS.append(self)

    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f" nome: {self.nome}\n"
            f" email: {self.email}"
        )

    @classmethod
    def criar_usuario(cls, nome, senha, email):
        usuario = User(len(USUARIOS) + 1, nome, senha, email)
        usuario.adicionar()
        return usuario

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
        evento = Event(len(EVENTOS) + 1, titulo, descricao, data, local, preco, self.id, self.nome)
        EVENTOS.append(evento)
        print(f"Evento '{titulo}' criado por {self.nome}!")
        return evento

    def editar_evento(self, id_evento, titulo=None, descricao=None, data=None, local=None, preco=None):
        for evento in EVENTOS:
            if evento.id == id_evento:
                if evento.id_usuario != self.id:
                    print("Você só pode editar seus próprios eventos!")
                    return
                if titulo: evento.titulo = titulo
                if descricao: evento.descricao = descricao
                if data: evento.data = data
                if local: evento.local = local
                if preco: evento.preco = preco
                print(f"Evento '{evento.titulo}' atualizado por {self.nome}!")
                return evento
        print("Evento não encontrado!")

    def deletar_evento(self, id_evento):
        for evento in EVENTOS:
            if evento.id == id_evento:
                if evento.id_usuario != self.id:
                    print("Você só pode deletar seus próprios eventos!")
                    return
                EVENTOS.remove(evento)
                print(f"Evento '{evento.titulo}' deletado por {self.nome}!")
                return
        print("Evento não encontrado!")

    def deletar_qualquer_evento(self, id_evento):
        for evento in EVENTOS:
            if evento.id == id_evento:
                EVENTOS.remove(evento)
                print(f"Evento '{evento.titulo}' deletado!")
                return
        print("Evento não encontrado!")

    def criar_cupom(self, titulo, desconto, validade, id_evento):
        for evento in EVENTOS:
            if evento.id == id_evento:
                if evento.id_usuario != self.id:
                    print("Você só pode criar cupons para seus próprios eventos!")
                    return
                cupom = Cupom(len(CUPONS) + 1, titulo, 10, validade, id_evento)
                CUPONS.append(cupom)
                print(f"Cupom '{titulo}' criado por {self.nome}!")
                return cupom
        print("Evento não encontrado!")

    def deletar_cupom(self, id_cupom):
        for cupom in CUPONS:
            if cupom.id == id_cupom:
                CUPONS.remove(cupom)
                print(f"Cupom '{cupom.titulo}' deletado!")
                return
        print("Cupom não encontrado!")

    @classmethod
    def listar_eventos(cls):
        return EVENTOS

    @classmethod
    def listar_cupons(cls):
        return CUPONS

