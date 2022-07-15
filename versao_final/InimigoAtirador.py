import pygame
from pygame.locals import *

from math import sin, cos, atan2, hypot
import os

import random as rd
from Settings import Settings
from Bala import Bala
from Inimigo import Inimigo


class InimigoAtirador(Inimigo):
    """
    Classe que define inimigos atiradores, que evitam o jogador e atiram
    projéteis de uma distância segura
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str,
                    velocidade_ataque: int, vida=10):
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
        
        self._velocidade_ataque = velocidade_ataque
        self._tempo_ultimo_tiro = 0
        self._tempo_ultimo_caminho = 0

        self._settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        """O InimigoAtirador vai atirar projéteis na direção do Jogador"""

        # obtém o tempo quando o método é chamado, para comparar com o tempo salvo
        # isso é a base do sistema de cadência de tiros  
        tempo_agora = pygame.time.get_ticks()

        # compara o tempo obtido com o tempo salvo para checar se está dentro do tempo de cadência
        if tempo_agora - self._tempo_ultimo_tiro > 5000:
            # atualiza o tempo
            self._tempo_ultimo_tiro = tempo_agora


            # calcula as distâncias da posição do jogador à posição do inimigo
            distancia_x = jogador_x - self._rect.x
            distancia_y = jogador_y - self._rect.y

            # calcula o ângulo entre essas distâncias e com isso calcula a velocidade do projétil
            angulo = atan2(distancia_y, distancia_x)

            speed_x = self._velocidade_ataque * cos(angulo)
            speed_y = self._velocidade_ataque * sin(angulo)

            # instancia uma nova Bala de acordo com as informações obtidas e retorna a mesma
            nova_bala = Bala(
                self._rect.x,
                self._rect.y,
                speed_x,
                speed_y,
                pygame.image.load(os.path.join(os.path.dirname(__file__), "assets" ,"isca.png")),
                3,
                20)

            return nova_bala

    def mover(self, x, y):
        # Move-se ao multiplicar os xs e ys obtidos pelo processo de normalização 
        # pela velocidade do inimigo
        self._rect.x += x * self._velocidade
        self._rect.y += y * self._velocidade
    
    def achar_caminho(self, jogador_x, jogador_y, raio=50) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - self._rect.x, jogador_y - self._rect.y
        hyp = hypot(distx, disty)

        # Normalizando as distâncias
        distx, disty = distx / hyp, disty / hyp
        tempo_agora = pygame.time.get_ticks()

        # Checando se o jogador está perto,
        # se sim, fugir dele
        # se não, caminho aleatório
        if abs(jogador_x - self._rect.x) <= raio:
            return -5*distx, -5*disty
        elif tempo_agora - self._tempo_ultimo_caminho >= 200:
            x = rd.choice([1, -1])
            y = rd.choice([1, -1])
            
            # Atualiza o tempo
            self._tempo_ultimo_caminho = tempo_agora
            
            return x, y
        
        return 0, 0
