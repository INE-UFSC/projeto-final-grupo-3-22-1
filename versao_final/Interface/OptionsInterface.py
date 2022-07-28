import pygame
import sys
from .Interface import Interface
from .ToMenuButton import ToMenuButton
from .Slider import Slider
from .Settings import Settings

settings = Settings()


class OptionsInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(
            "Interface/options_background.png"
        )
        self.__buttons_list = [ToMenuButton(510, 590, "Voltar"),
                            ToMenuButton(790, 590, "Confirmar")]
        self.__slider = Slider(600, 200)

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list

    @property
    def slider(self):
        return self.__slider

    def interfaceLoop(self):
        self.settings.screen.blit(self.background, (0, 0))
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for button in self.buttons_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button.nextStep(pygame.mouse.get_pos())
                    button.changeColor(pygame.mouse.get_pos())

                    button.update()
                
                self.slider.draw_slider()

            pygame.display.update()
