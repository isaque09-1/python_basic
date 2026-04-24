from db import EVENTOS

class Cupom:
    def __init__(self, id, titulo, desconto, validade, id_evento):
        self.id = id
        self.titulo = titulo
        self.desconto = desconto
        self.validade = validade
        self.id_evento = id_evento


    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f" titulo: {self.titulo}\n"
            f" desconto: {self.desconto}%\n"
            f" validade: {self.validade}\n"
            f" id_evento: {self.id_evento}"
        )
