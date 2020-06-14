from agentes.modelagem.problema import ProblemaAbstrato

class ProblemaClassificador(ProblemaAbstrato):
    def __init__(self, estado_inicial):
        super().__init__()
        self._estado_inicial = estado_inicial

    def estado_inicial(self):
        return self._estado_inicial
    
    def acoes(self, estado):
        """ supondo q estado já é uma tupla de valores """
        from acoes import AcaoJogador

        todas_acoes = []
        cima, baixo, esquerda, direita = "cima", "baixo", "esquerda", "direita"
        todas_acoes.extend([AcaoJogador.puxar(cima), AcaoJogador.puxar(baixo), AcaoJogador.puxar(esquerda), AcaoJogador.puxar(direita)])
        
        return todas_acoes
    
    def resultado(self, estado, acao):
        from acoes import AcoesJogador
        import numpy as np

        estado_resultante = np.array(estado)

        coord_vazio = np.where(estado_resultante == 0)
        lin = coord_vazio[0][0]
        col = coord_vazio[1][0]

        if acao.tipo == AcoesJogador.PUXAR:
            direcao = acao.parametros
            if direcao == "cima":
                if (lin-1) >= 0:
                    estado_resultante[lin][col], estado_resultante[lin-1][col] = estado_resultante[lin-1][col], estado[lin][col]

            elif direcao == "baixo":
                if (lin+1) <= 2:
                    estado_resultante[lin][col], estado_resultante[lin+1][col] = estado_resultante[lin+1][col], estado_resultante[lin][col]

            elif direcao == "esquerda":
                if (col-1) >= 0:
                    estado_resultante[lin][col], estado_resultante[lin][col-1] = estado_resultante[lin][col-1], estado_resultante[lin][col]

            elif direcao == "direita":
                if (col+1) <= 2:
                    estado_resultante[lin][col], estado_resultante[lin][col+1] = estado_resultante[lin][col+1], estado_resultante[lin][col]
        else:
            raise TypeError

        return tuple(estado_resultante)
    
    def teste_objetivo(self, estado):
        import numpy as np
        final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        #estado_resultante = list(estado)
        return all(estado[i][j] == final[i][j] for i in range(0,3) for j in range(0,3))

    def custo_transicao(self, estado, acao, estado_resultante):
        return 1