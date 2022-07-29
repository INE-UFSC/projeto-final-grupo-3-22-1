from Button import Button
from Settings import Settings


class ContinueButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)
        self.__settings = Settings()

    @property
    def settings(self) -> Settings:
        return self.__settings

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            #trocar pela função do main loop que será criada na interface InGame
            self.settings.paused = False
