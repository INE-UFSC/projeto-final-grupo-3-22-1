import pygame
import csv
from Jogador import Jogador

tilemap = ["BBBBBBBBBB",
"B........B",
"B........B",
"B........B",
"B...P....B",
"B........B",
"B........B",
"B........B",
"B........B",
"BBBBBBBBBB"]

class Bloco(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.x = x * 64
        self.y = y * 64
        self.width = 64
        self.height = 64
        self.jogo = jogo
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((242, 196, 56))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.grupos = self.jogo.sprites, self.jogo.blocks
        pygame.sprite.Sprite.__init__(self, self.grupos)

class jogo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,640))
        self.clock = pygame.time.Clock()
        self.running = True

        self.sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

        self.criarMapa()

    def criarMapa(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Bloco(self, j,i)


    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def desenhar(self):
        self.screen.fill((0,150,0))
        self.sprites.draw(self.screen)
        self.clock.tick(60)
        pygame.display.update()

    def atualizar(self):
        self.sprites.update()

    def rodar(self):
        while self.running:
            self.eventos()
            self.desenhar()
            self.atualizar()

g = jogo()

while g.running:
    g.rodar()

