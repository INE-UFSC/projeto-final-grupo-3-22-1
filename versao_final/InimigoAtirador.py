import pygame
from pygame.locals import *

from math import sin, cos, atan2, hypot

import random as rd
from Settings import Settings
from Globals import Globals
from Bala import Bala
from Inimigo import Inimigo
from BombaTinta import BombaTinta

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

        self._centrox = (self._rect.x + (self._sprite.get_width() / 2)) 
        self._centroy = (self._rect.y + (self._sprite.get_height() / 2))

        self._settings = Settings()
        self._globals = Globals()

    def atacar(self, jogador_x, jogador_y):
        """O InimigoAtirador vai atirar projéteis na direção do Jogador"""

        # se o jogador está muito próximo, joga uma mancha de tinta nos arredores
        distx, disty = jogador_x - self._rect.x, jogador_y - self._rect.y
        hipotenusa = hypot(disty, distx)

        if hipotenusa > 100:
            return self._ataque_distancia(jogador_x, jogador_y)

        return self._ataque_proximo(
            (self._rect.x + (self._sprite.get_width() / 2)), 
            (self._rect.y + (self._sprite.get_height() / 2))
        )

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

    def _ataque_distancia(self, jogador_x, jogador_y):
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
                pygame.image.load("assets/isca.png"),
                3,
                20)

            return nova_bala
    
    def _ataque_proximo(self, x, y):
            
            tempo_agora = pygame.time.get_ticks()
            
            if tempo_agora - self._tempo_ultimo_caminho > 1500:
                self._tempo_ultimo_caminho = tempo_agora

                bomba_tinta = BombaTinta(
                    x,
                    y,
                    pygame.image.load("assets/mancha_tinta.png"),
                    25
                )

                return bomba_tinta