import pygame
from pygame.locals import *
from math import sin, cos, atan2, degrees

from Arma import Arma
from Bala import Bala
from PowerUp import PowerUp
from PowerUpPermanente import PowerUpPermanente
from PowerUpTemporario import PowerUpTemporario

from Settings import Settings
from Globals import Globals


class Jogador(pygame.sprite.Sprite):
    def __init__(
        self,
        vida: int,
        velocidade_movimento: int,
        arma: Arma = Arma(20, 4, 250, "isca", 1),
    ):
        super().__init__()
        self.__stats = {"vida": vida, "velocidade_movimento": velocidade_movimento}

        self.__arma = arma
        self.__morto = False

        self.__sprite = pygame.image.load("assets/ChicoCunha.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (
            int(self.sprite.get_width() / 2),
            int(self.sprite.get_height() / 2),
        )

        self.__tempo_ultimo_tiro = 0

        self.__powerUps_temporarios = []
        self.__powerUps_permanentes = []

        self.__settings = Settings()
        self.__globals = Globals()

    @property
    def stats(self) -> dict:
        return self.__stats

    @property
    def morto(self) -> bool:
        return self.__morto

    @morto.setter
    def morto(self, estado: bool):
        self.__morto = estado

    @property
    def x(self) -> int:
        return self.__rect.x

    @property
    def y(self) -> int:
        return self.__rect.y

    @property
    def arma(self) -> Arma:
        return self.__arma

    @arma.setter
    def arma(self, arma):
        self.__arma = arma

    @property
    def sprite(self):
        return self.__sprite

    def set_sprite(self, sprite):
        self.__sprite = pygame.image.load(sprite)

    @property
    def rect(self):
        return self.__rect

    @property
    def tempo_ultimo_tiro(self) -> int:
        return self.__tempo_ultimo_tiro

    @tempo_ultimo_tiro.setter
    def tempo_ultimo_tiro(self, tempo):
        self.__tempo_ultimo_tiro = tempo

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def globals(self) -> Globals:
        return self.__globals

    @property
    def powerUps_temporarios(self):
        return self.__powerUps_temporarios

    @property
    def powerUps_permanentes(self):
        return self.__powerUps_permanentes

    def mover(self):
        # TODO: animacao de acordo com andando
        self.__andando = False
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-(self.stats["velocidade_movimento"]), 0)
                self.__andando = True

        if self.rect.right < self.settings.largura_tela:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(self.stats["velocidade_movimento"], 0)
                self.__andando = True

        if self.rect.bottom < self.settings.largura_tela:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0, self.stats["velocidade_movimento"])
                self.__andando = True

        if self.rect.top > 0:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -(self.stats["velocidade_movimento"]))
                self.__andando = True

    def atirar(self, mouse_x, mouse_y):
        tempo_agora = pygame.time.get_ticks()

        if tempo_agora - self.__tempo_ultimo_tiro > self.arma.stats["cadencia"]:
            self.__tempo_ultimo_tiro = tempo_agora

            distancia_x = mouse_x - self.rect.x
            distancia_y = mouse_y - self.rect.y

            angulo = atan2(distancia_y, distancia_x)

            speed_x = self.arma.stats["velocidade_projetil"] * cos(angulo)
            speed_y = self.arma.stats["velocidade_projetil"] * sin(angulo)

            nova_bala = Bala(
                self.rect.x,
                self.rect.y,
                speed_x,
                speed_y,
                pygame.transform.rotate(self.arma.sprite_bala, -degrees(angulo) - 90),
                self.arma.stats["dano"],
                self.arma.stats["durabilidade_bala"],
            )

            return nova_bala

    def mover_arma(self, mouse_x, mouse_y):
        dist_x = mouse_x - self.rect.x
        dist_y = mouse_y - self.rect.y
        angulo = atan2(dist_y, dist_x)

        copia_arma = pygame.transform.rotate(
            self.arma.sprite_bala, -degrees(angulo) - 90
        )

        self.globals.DISPLAY_SURF.blit(
            copia_arma,
            (
                self.x + self.sprite.get_width() - 10 - int(copia_arma.get_width() / 2),
                (self.y + self.sprite.get_height() - 3 - int(copia_arma.get_height())),
            ),
        )

    def receber_dano(self, dano: int):
        self.stats["vida"] -= dano

        if self.stats["vida"] <= 0:
            self.morrer()

    def morrer(self):
        self.__morto = True

        self.set_sprite("assets/ChicoCunhaMorto.png")
        pygame.display.set_caption("Fim de jogo.")
        self.globals.DISPLAY_SURF.fill((255, 255, 255))
        self.globals.DISPLAY_SURF.blit(self.sprite, self.rect)

    # adiciona a lista de power-up daquele tipo; controlePowerUps faz lógica
    def usar_powerUp(self, powerUp: PowerUp):
        powerUp.tempo_pego = pygame.time.get_ticks()

        if isinstance(powerUp, PowerUpPermanente):
            self.powerUps_permanentes.append(powerUp)
        elif isinstance(powerUp, PowerUpTemporario):
            self.powerUps_temporarios.append(powerUp)

        for stat, value in powerUp.mudancas.items():
            if stat in self.stats.keys():
                self.stats[stat] += value
            else:
                self.arma.stats[stat] += value

    def encerrar_powerUp(self, powerUp):
        for stat, value in powerUp.mudancas.items():
            if stat in self.stats.keys():
                self.stats[stat] -= value
            else:
                self.arma.stats[stat] -= value

        self.powerUps_temporarios.remove(powerUp)
