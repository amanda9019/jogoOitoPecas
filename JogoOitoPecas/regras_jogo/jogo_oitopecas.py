from regras_jogo.regras_abstratas import AbstractRegrasJogo

class JogoOitoPecas(AbstractRegrasJogo):

    def __init__(self):
        #from random import randint
        import random
        import numpy as np
        
        self.movimentos = 0

        numeros = [1,2,3,4,6,8,7,5,0]  #exemplo facil
        #numeros = [5,3,1,4,0,6,7,8,2]  #exemplo2

        #numeros = random.sample(range(0,9), 9)
        #print(numeros) #teste
        arrs = []

        # Converte a lista em uma lista bidimensional
        for i in range(0,3):
            while len(numeros) >= 1:
                pedaco = numeros[i*3:(i*3)+3]
                arrs.append(pedaco)
                numeros = numeros[(i*3)+3:]

        self.elementos = arrs                       #Ex: [[1, 2, 3], [4, 6, 8], [7, 5, 0]]
        # Converte em numpy array
        self.elementos = np.array(self.elementos)   #Ex: [[1 2 3][4 6 8][7 5 0]]


    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return 1
    
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        import numpy as np
        final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        #print(final) #teste
        return all(self.elementos[i][j] == final[i][j] for i in range(0,3) for j in range(0,3))


    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return {"disposicao": tuple(self.elementos)}

    def registrarProximaAcao(self, id_agente, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acao_jogador = acao

    def atualizarEstado(self, tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        from acoes import AcoesJogador
        import numpy as np

        coord_vazio = np.where(self.elementos == 0)  #ex: [[2],[2]]
        lin = coord_vazio[0][0]  #o primeiro elem do primeiro array (2)
        col = coord_vazio[1][0]  #o primeiro elem do segundo array (2)

        if self.acao_jogador.tipo == AcoesJogador.PUXAR:
            direcao = self.acao_jogador.parametros
            if direcao == "cima":
                if (lin-1) >= 0:
                    self.elementos[lin][col], self.elementos[lin-1][col] = self.elementos[lin-1][col], self.elementos[lin][col]
                    self.movimentos += tempo
                else:
                    print('Não há peça acima do espaço vazio! Tente novamente.')

            elif direcao == "baixo":
                if (lin+1) <= 2:
                    self.elementos[lin][col], self.elementos[lin+1][col] = self.elementos[lin+1][col], self.elementos[lin][col]
                    self.movimentos += tempo
                else:
                    print('Não há peça abaixo do espaço vazio! Tente novamente.')

            elif direcao == "esquerda":
                if (col-1) >= 0:
                    self.elementos[lin][col], self.elementos[lin][col-1] = self.elementos[lin][col-1], self.elementos[lin][col]
                    self.movimentos += tempo
                else:
                    print('Não há peça a esquerda do espaço vazio! Tente novamente.')

            elif direcao == "direita":
                if (col+1) <= 2:
                    self.elementos[lin][col], self.elementos[lin][col+1] = self.elementos[lin][col+1], self.elementos[lin][col]
                    self.movimentos += tempo
                else:
                    print('Não há peça a direita do espaço vazio! Tente novamente.')
        else:
            raise TypeError

        #self.movimentos += tempo

    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        print(f'Parabéns! Você terminou o jogo num total de {self.movimentos} movimentos! :D')
