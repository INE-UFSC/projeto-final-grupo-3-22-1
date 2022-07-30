import pygame

class Terreno(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteLocal:pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.x = x * 32
        self.y = y * 32
        self.width = 64
        self.height = 64
        self.image = spriteLocal
        self.sprite = self.image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y