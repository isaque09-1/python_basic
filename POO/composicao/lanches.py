from typing import List


class Lanche:
    def __init__(self, nome: str, descricao: str, preco: float):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __repr__(self):
        return f"Lanche(nome={self.nome}, descricao={self.descricao}, preco={self.preco})"


class LanchesDisponiveis:
    def padrao():
        return [
            Lanche("Sanduíche", "Pão, carne e queijo", 18.0),
            Lanche("Salgado", "Coxinha", 8.0),
            Lanche("Refrigerante", "Lata 350ml", 7.0),
            Lanche("Água", "Garrafa 500ml", 4.0),
        ]

