import pygame
import sys
from Interface import Interface
from ToMenuButton import ToMenuButton
from Settings import Settings

settings = Settings()

class GameOverInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__font = pygame.font.Font(f"fonts/alterebro-pixel-font.ttf", 38)
        self.__line1_render = self.font.render("Você não foi capaz de ajudar Chico Cunha.", True, (0,0,0))
        self.__line2_render = self.font.render("Reflita sobre suas atitudes e tente novamente.", True, (0,0,0))
        self.__background = pygame.image.load(
            "backgrounds/game_over_background.png"
        )
        self.__buttons_list = [ToMenuButton(665, 450, "Menu Principal")
                            ]
        self.__clock = pygame.time.Clock()
        self.__song = "songs/game_over_song.mp3"

    @property
    def font(self):
        return self.__font

    @property
    def font2(self):
        return self.__font2

    @property
    def line1_render(self):
        return self.__line1_render

    @property
    def line2_render(self):
        return self.__line2_render

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list
    
    @property
    def clock(self):
        return self.__clock

    @property
    def song(self):
        return self.__song

    def interfaceLoop(self):
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for button in self.buttons_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button.nextStep(pygame.mouse.get_pos())
                    button.changeColor(pygame.mouse.get_pos())

            self.settings.screen.blit(self.background, (0, 0))
            self.settings.screen.blit(self.line1_render, (525, 310))
            self.settings.screen.blit(self.line2_render, (500, 340))
            for button in self.buttons_list:
                button.update()

            pygame.display.update()