#!/usr/bin/env python3

import time
from regras_jogo.regras_abstratas import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    print("Bem vindo ao jogo 8 Puzzle!")
    # Seletor de jogador, permitindo escolher qual agente
    jogador = input("Selecione o jogador: ")
    tipo_agente = input("Selecione o agente: ")

    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    #agente_jogador = construir_agente(TiposAgentes.AUTO_BFS, Personagens.O_JOGADOR)
    agente_jogador = construir_agente(tipo_agente, jogador)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador (Printa a lista de elementos)
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo (Pede input do jogador e armazena a ação desejada)
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo (Realiza a ação desejada armazenada)
        tempo_corrente = ler_tempo(em_turnos=True)
        #jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        jogo.atualizarEstado(tempo_corrente)
        tempo_de_jogo += tempo_corrente

    # Mostra o estado final seguido da mensagem de finalização
    agente_jogador.adquirirPercepcao(ambiente_perceptivel)
    jogo.terminarJogo()


if __name__ == '__main__':
    iniciar_jogo()
