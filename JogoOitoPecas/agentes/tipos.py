from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'

    AUTO_DLS = 'Automático DLS'
    AUTO_IDDFS = 'Automático IDDFS'
    AUTO_GULOSO = 'Automático Guloso'
    AUTO_A_ESTRELA = 'Automático A-Estrela'
    
    # adicionar outros tipos de agentes de acordo com
    # o necessário