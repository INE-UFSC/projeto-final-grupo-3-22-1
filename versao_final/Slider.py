import pygame
from Settings import Settings

settings = Settings()

class Slider():
    def __init__(self, pos_x, pos_y):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.mouse_x = 0
        self.surface = pygame.display.get_surface()
        self.initial_rectangle = pygame.draw.rect(self.surface,(0,0,0),pygame.Rect(self.pos_x+self.mouse_x,self.pos_y,10,20))

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    def draw_slider(self):
        self.pressed = pygame.mouse.get_pressed()
        self.pos = pygame.mouse.get_pos()
        slider = pygame.draw.rect(self.surface,((60,23,82)),pygame.Rect(self.pos_x,self.pos_y,300,20))
        if self.pressed[0] != 0 and self.pos[0] in range(slider.left, slider.right) and self.pos[1] in range(slider.top, slider.bottom):
            mouse_x = self.pos[0]
            a = mouse_x
            if a < 0:
                a = 0
            elif a > self.pos_x + 290:
                a = self.pos_x + 290

            pygame.draw.rect(self.surface,(0,0,0),pygame.Rect(a,self.pos_y,10,20))
