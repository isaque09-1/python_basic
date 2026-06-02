from typing import Any, Dict, List, Optional

from POO.composicao.event import Event
from POO.composicao.palestrantes import Palestrante
from POO.composicao.lanches import Lanche, LanchesDisponiveis


class Cronograma:
    def __init__(
        self,
        eventos: Optional[List[Event]] = None,
        palestrantes: Optional[List[Palestrante]] = None,
        horario: str = "",
        lanches_disponiveis: Optional[List[Lanche]] = None,
    ):
        self.eventos = eventos or []
        self.palestrantes = palestrantes or []
        self.horario = horario
        self.lanches_disponiveis = (
            lanches_disponiveis if lanches_disponiveis is not None else LanchesDisponiveis.padrao()
        )
        self.itens: List[Dict[str, Any]] = []

    def __repr__(self):
        return f"Cronograma(horario={self.horario}, eventos={len(self.itens)})"

    def add_evento(self, evento: Event, palestrantes_evento: Optional[List[Palestrante]] = None, lanches: Optional[List[Lanche]] = None):
        pls = palestrantes_evento or []
        lns = lanches or list(self.lanches_disponiveis)
        item = {"evento": evento, "palestrantes": pls, "lanches": lns}
        self.itens.append(item)
        return item

    def adicionar_palestrante_ao_evento(self, evento: Event, palestrante: Palestrante):
        for item in self.itens:
            if item["evento"] is evento:
                item["palestrantes"].append(palestrante)
                return
        self.add_evento(evento, palestrantes_evento=[palestrante])

    def get_palestrantes_por_evento(self, evento: Event):
        for item in self.itens:
            if item["evento"] is evento:
                return item["palestrantes"]
        return []

    def get_lanches_por_evento(self, evento: Event):
        for item in self.itens:
            if item["evento"] is evento:
                return item["lanches"]
        return []

    @classmethod
    def criar_cronograma(cls,data: dict,eventos: List[Event],palestrantes: List[Palestrante],horario: str,):
        cronograma = cls(horario=horario)
        lanches = data("lanches")
        for evento in eventos:
            cronograma.add_evento(evento, palestrantes_evento=palestrantes, lanches=lanches)
        return cronograma

