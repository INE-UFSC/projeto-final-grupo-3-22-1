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
        self.__font = pygame.font.Font(f"fonts/alterebro-pixel-font.ttf", 32)
        self.__line1_render = self.font.render("Olá, meu nome é Chico Cunha e sou pescador. Costumo viver em paz, mas", True, (0,0,0))
        self.__line2_render = self.font.render("ultimamente as criaturas do mar têm se revoltado contra mim e preciso", True, (0,0,0))
        self.__line3_render = self.font.render("da sua ajuda para contê-las. Mas antes gostaria de saber seu nome:", True, (0,0,0))
        self.__background = pygame.image.load(
            "backgrounds/name_input_background.png"
        )
        self.__buttons_list = [ToMenuButton(510, 590, "Voltar"),
                            ToMenuButton(790, 590, "Confirmar")]
        self.__text_input = TextInput(600, 350, 300, 32, "Digite seu nome aqui")
        self.__clock = pygame.time.Clock()

    @property
    def font(self):
        return self.__font

    @property
    def line1_render(self):
        return self.__line1_render

    @property
    def line2_render(self):
        return self.__line2_render

    @property
    def line3_render(self):
        return self.__line3_render

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list

    @property
    def text_input(self):
        return self.__text_input
    
    @property
    def clock(self):
        return self.__clock

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

            self.settings.screen.blit(self.background, (0, 0))
            self.settings.screen.blit(self.line1_render, (350, 140))
            self.settings.screen.blit(self.line2_render, (355, 170))
            self.settings.screen.blit(self.line3_render, (365, 200))
            self.text_input.desenhar(settings.screen)
            pygame.display.update()
