import pygame
from pygame.locals import *

from math import hypot, degrees, atan2

from Settings import Settings
from Inimigo import Inimigo


class InimigoDirecional(Inimigo):
    """
    Classe que define inimigos atiradores, que evitam o jogador e atiram
    projéteis de uma distância segura
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str, vida=10):
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
        
        self._tempo_ultimo_tiro = 0
        self._tempo_ultimo_caminho = 0
        self._inicio_movimento = True
        self._sprite_original = self._sprite

        self._ultima_distx = self._ultima_disty = 0

        self._settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        pass     

    def mover(self, x, y):
        # Move-se ao multiplicar os xs e ys obtidos pelo processo de normalização 
        # pela velocidade do inimigo
        self._rect.x += x * self._velocidade
        self._rect.y += y * self._velocidade
    
    def achar_caminho(self, jogador_x, jogador_y) -> int:
        # Checando se o inimigo atingiu a parede
        atingiuParede = False
        if self._rect.x >= self._settings.largura_tela or self._rect.x <= 0:
            atingiuParede = True
        if self._rect.y >= self._settings.altura_tela or self._rect.y <= 0:
            atingiuParede = True

        if self._inicio_movimento:
            # Achando os catetos e a hipotenusa
            distx, disty = jogador_x - self._rect.x, jogador_y - self._rect.y
            hyp = hypot(distx, disty)

            # Normalizando as distâncias e colocando-as em um vetor base,
            # que não será atualizado a não ser que o inimigo atinja uma parede
            distx, disty = distx / hyp, disty / hyp
            self._inicio_movimento = False
            
            self._ultima_distx = distx
            self._ultima_disty = disty

            angulo = atan2(disty, distx)

            # Rotaciona o sprite de acordo com o ângulo relativo ao jogador,
            # de modo que sempre estará apontando ao mesmo quando atinge uma parede
            self._sprite = pygame.transform.rotate(self._sprite, -degrees(angulo) - 90)

        if atingiuParede:
            # Atualizando o sprite para o sprite original, facilita os cálculos
            self._sprite = self._sprite_original
            
            # Achando os catetos e a hipotenusa
            distx, disty = jogador_x - self._rect.x, jogador_y - self._rect.y
            hyp = hypot(distx, disty)

            angulo = atan2(disty, distx)

            # Rotaciona o sprite de acordo com o ângulo relativo ao jogador
            self._sprite = pygame.transform.rotate(self._sprite, -degrees(angulo) - 90)

            # Normalizando as distâncias
            distx, disty = distx / hyp, disty / hyp
            
            self._ultima_distx, self._ultima_disty = distx, disty

            return distx, disty
        
        return self._ultima_distx, self._ultima_disty