from Button import Button
from Settings import Settings
from RankingInterface import RankingInterface

settings = Settings
ranking = RankingInterface()

class RankingButton(Button):
    def __init__(self, pos_x, pos_y, text_input):
        super().__init__(pos_x, pos_y, text_input)

    def nextStep(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            ranking.interfaceLoop()
