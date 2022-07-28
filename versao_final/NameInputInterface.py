import pygame
import sys
from Interface import Interface
from ToMenuButton import ToMenuButton
from TextInput import TextInput
from Settings import Settings

settings = Settings()

class NameInputInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(
            "backgrounds/options_background.png"
        )
        self.__buttons_list = [ToMenuButton(510, 590, "Voltar"),
                            ToMenuButton(790, 590, "Confirmar")]
        self.__text_input = TextInput(490, 400, 300, 32, "Digite seu nome aqui")

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list

    @property
    def text_input(self):
        return self.__text_input

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

                self.text_input.event_handler(event)

            self.text_input.desenhar(settings.screen)
            pygame.display.update()
