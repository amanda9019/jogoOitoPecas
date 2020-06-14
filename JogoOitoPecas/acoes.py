from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    PUXAR = 'puxar'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def puxar(cls, direcao):
        return cls(AcoesJogador.PUXAR, (direcao))