from typing import Any, List, Optional

from event import Event
from palestrantes import Palestrante


class Cronograma:
    def __init__(self,eventos: Optional[List[Event]] = None,palestrantes: Optional[List[Palestrante]] = None,horario: str = "",):
        self.eventos = eventos if eventos is not None else []
        self.palestrantes = palestrantes if palestrantes is not None else []
        self.horario = horario

    @classmethod
    def criar_cronograma(cls,eventos: List[Event],palestrantes: List[Palestrante],horario: str,):
        return cls(eventos=eventos,palestrantes=palestrantes,horario=horario,)

