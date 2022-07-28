import pygame
import random as rd
from Settings import Settings
from Globals import Globals
from Bala import Bala
from BombaVeneno import BombaVeneno
from BombaLava import BombaLava

class Boss():
    def __init__(self, x: int, y: int, dano: int,
                    vida: int, sprite: str,
                    vel_mov: int , vel_atq: int):
        self._dano = dano
        self._vel_mov = vel_mov
        self._vel_atq = vel_atq
        self._vida = vida
        self._sprite = pygame.image.load(sprite)
        self._rect = self._sprite.get_rect(center=(x, y))

        self._settings = Settings()
        self._globals = Globals()

        self._tempo_comeco_ataque = 0 

    def atacar(self):
        pass

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
            incr = -0.05
            balas_boss = []
            for _ in range(5):
                nova_bala = Bala(
                    self._rect.x,
                    self._rect.y,
                    speed_x+incr,
                    speed_y+incr,
                    pygame.image.load("assets/isca.png"),
                    3,
                    20)
                
                incr += 0.25
                balas_boss.append(nova_bala)

            return balas_boss
        
    def _ataque_proximo(self, x, y):
            
        tempo_agora = pygame.time.get_ticks()

        signal = 1
        while tempo_agora - self._tempo_comeco_ataque <= 500:
            self._rect.x += signal
            self._rect.y += signal
            signal *= -1
        
        return BombaVeneno(
            x,
            y,
            pygame.image.load("assets/mancha_veneno.png"),
            5
        )
    
    def _ataque_especial(self, x, y):

        tempo_agora = pygame.time.get_ticks()
        
        signal = 1
        while tempo_agora - self._tempo_comeco_ataque <= 500:
            self._rect.x += signal*5
            signal *= -1

        return BombaLava(
            x+rd.choice([-7, -5, -2, 2, 5, 7]),
            y+rd.choice([-7, -5, -2, 2, 5, 7]),
            pygame.image.load("assets/mancha_lava.png"),
            5
        )
