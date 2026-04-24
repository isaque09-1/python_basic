from db import EVENTOS

class Cupom:
    def __init__(self, id, titulo, desconto, validade, id_evento):
        self.id = id
        self.titulo = titulo
        self.desconto = desconto
        self.validade = validade
        self.id_evento = id_evento

    def evento(self):
        for evento in EVENTOS:
            if evento.id == self.id_evento:
                return evento
        return None

    def __repr__(self):
        evento = self.evento()
        evento_titulo = evento.titulo if evento else "Evento não encontrado"
        return (
            f"id: {self.id}\n"
            f" titulo: {self.titulo}\n"
            f" desconto: {self.desconto}%\n"
            f" validade: {self.validade}\n"
            f" evento: {evento_titulo}"
        )

