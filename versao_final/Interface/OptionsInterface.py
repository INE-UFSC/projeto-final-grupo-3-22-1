import pygame
<<<<<<< HEAD
from Interface import Interface
from ToMenuButton import ToMenuButton
from Settings import Settings
=======
import sys
from .Interface import Interface
from .ToMenuButton import ToMenuButton
from .Settings import Settings
>>>>>>> 5c18f917f25205c1426b2e678afdadf448890915

settings = Settings()


class OptionsInterface(Interface):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.__background = pygame.image.load(f'./options_background.png')
        self.__buttons_list = [ToMenuButton(510, 590, "Voltar"),
                            ToMenuButton(790, 590, "Confirmar")]
=======
        self.__options_background = pygame.image.load(
            "Interface/options_background.png"
        )
>>>>>>> 5c18f917f25205c1426b2e678afdadf448890915

    @property
    def background(self):
        return self.__background

<<<<<<< HEAD
    @property
    def buttons_list(self):
        return self.__buttons_list
=======
    @options_background.setter
    def options_background(self, options_background):
        self.__options_background = options_background

    def interfaceLoop(self):
        while True:
            return_button = ToMenuButton(510, 590, "Voltar")
            confirm_button = ToMenuButton(790, 590, "Confirmar")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return_button.nextStep(pygame.mouse.get_pos())
                    confirm_button.nextStep(pygame.mouse.get_pos())

            settings.screen.blit(self.options_background, (0, 0))

            return_button.changeColor(pygame.mouse.get_pos())
            confirm_button.changeColor(pygame.mouse.get_pos())

            return_button.update()
            confirm_button.update()

            pygame.display.update()
>>>>>>> 5c18f917f25205c1426b2e678afdadf448890915
