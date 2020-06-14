class No():
    def __init__(self, estado, acao=None, gn=0, pai=None):
        self.estado = estado
        self.acao = acao
        self.gn = gn
        self.pai = pai
    
    def calcularProfundidade(self):
        raiz = not self.pai
        return 0 if raiz else self.pai.calcularProfundidade() + 1
    
    def extrairSolucao(self):
        if self.pai == None:
            return []
        else:
            return self.pai.extrairSolucao() + [self.acao]

    @staticmethod
    def novoNoFilho(problema, pai, acao):
        novo_estado = problema.resultado(pai.estado, acao)
        gn = pai.gn + problema.custo_transicao(pai.estado, acao, novo_estado)
        return No(novo_estado, acao, gn, pai)
