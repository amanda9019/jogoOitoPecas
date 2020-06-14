from agentes.humano import AgentePrepostoESHumano
class AgenteClassificadorBFS(AgentePrepostoESHumano):
    
    def __init__(self):
        self.seq = []
        self.objetivo = None

    def formularProblema(self):
        """ Formula um novo problema a ser resolvido, com base no objetivo atual.
            Ao final, self.problema deve estar preenchido.
        """
        from agentes.modelagem.classificador import ProblemaClassificador
        self.problema = ProblemaClassificador(self.percepcao_mundo)



    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        super().adquirirPercepcao(percepcao_mundo)  #Pega o esquema de print do agente preposto humano
        self.percepcao_mundo = percepcao_mundo['disposicao']
    
    def escolherProximaAcao(self):
        from agentes.buscas.buscas import busca_arvore

        # Se seq estiver vazia
        if not self.seq:  #Se não tiver uma sequencia de ações
            self.formularProblema()
            agente = "bfs"
            no_solucao = busca_arvore(self.problema, agente)  #Busca pela árvore o nó solução(estado final)
            self.seq = no_solucao.extrairSolucao()  #Obtem a sequencia de movimentos até a solução

        acao = self.seq.pop(0)  #Se tiver uma sequencia, pega a primeira ação q será a proxima ação
        print(f'O agente BFS escolheu: {acao.parametros}')
        print("")
        return acao

