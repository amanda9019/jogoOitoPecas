from abc import ABC, abstractmethod

class ProblemaAbstrato(ABC):

    @abstractmethod
    def estado_inicial(self):
        return
    
    @abstractmethod
    def acoes(self, estado):
        return
    
    @abstractmethod
    def resultado(self, estado, acao):
        return
    
    @abstractmethod
    def teste_objetivo(self, estado):
        return

    @abstractmethod
    def custo_transicao(self, estado, acao, estado_resultante):
        return