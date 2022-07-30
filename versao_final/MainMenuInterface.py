import pygame
import sys
from Interface import Interface
from PlayButton import PlayButton
from OptionsButton import OptionsButton
from ControlsButton import ControlsButton
from RankingButton import RankingButton
from QuitButton import QuitButton


class MainMenuInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(
            f"backgrounds/main_menu_background.png"
        )
        self.__buttons_list = [PlayButton(665, 220, "Jogar"), 
                            OptionsButton(665, 320, "Opções"),
                            ControlsButton(665, 420, "Controles"),
                            RankingButton(665, 520, "Ranking"),
                            QuitButton(665, 620, "Sair")]
        self.__song = "songs/game_soundtrack.mp3"

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self) -> list:
        return self.__buttons_list

    @property
    def song(self):
        return self.__song

    def interfaceLoop(self):
        self.settings.screen.blit(self.background, (0, 0))
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.settings.volume_musica)

        iniciar_jogo = False
        while not iniciar_jogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for button in self.buttons_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        comecou = button.nextStep(pygame.mouse.get_pos())
                        
                        if comecou:
                            print("aqui dentor")
                            iniciar_jogo = True
                            break
                    button.changeColor(pygame.mouse.get_pos())

                    button.update()
                pygame.display.update()
                break
            
            if iniciar_jogo:
                print(64)
                break
        return True

   
