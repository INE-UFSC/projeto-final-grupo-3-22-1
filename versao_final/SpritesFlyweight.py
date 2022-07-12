import pygame

class SpritesFlyweight:
    def __init__(self, address):
        self.spriteAddress = pygame.image.load(address)