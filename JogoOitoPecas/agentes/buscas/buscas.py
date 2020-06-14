from agentes.buscas.no_busca import No

def busca_arvore(problema, tipo_agente):
    """ Monta uma nova sequencia de acoes para resolver o problema atual.
        Ao final, self.seq deve estar preenchido.
    """
    borda = [ No(problema.estado_inicial()) ]
    while borda:  #Enquanto tiver nós na borda

        # 1- Distingue entre BFS e DFS
        if tipo_agente == "bfs":
            folha = borda.pop(0)                                #Pega o primeiro elemento da borda
        elif tipo_agente == "dfs":
            folha = borda.pop()                                 #Pega o último da borda
        else:
            raise ValueError('Agente de busca inválido!')

        # 2- Verifica se o nó atual é o objetivo, se for ele é retornado pois é o nó solução
        if problema.teste_objetivo(folha.estado):
            return folha

        # 3- Procede se o nó atual não for o objetivo
        for acao in problema.acoes(folha.estado):               #Percorre o estado (nó) resultante de cada ação
            expandido = No.novoNoFilho(problema, folha, acao)   #Abre os nós filhos
            borda.append(expandido)                             #E os adicionam na borda

    raise ValueError('Problema sem solução!')