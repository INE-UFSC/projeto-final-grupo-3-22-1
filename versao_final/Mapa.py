import pygame
from Bloco import Bloco
from terreno import Terreno
from SpritesFlyweight import SpritesFlyweight

class Mapa:
    def __init__(self, nome: str, numero_de_ondas: int, primeiro_mapa):
        self.__nome = nome
        self.__numero_de_ondas = numero_de_ondas
        self.__lista_de_inimigos = []
        self.__tilemap = primeiro_mapa
        self.__spriteCaixa = SpritesFlyweight("assets/caixa1.png")
        self.__spriteChao = SpritesFlyweight("assets/chão_normal.png")
        self.__background_sprites = pygame.sprite.RenderUpdates()
        self.sprite_blocks = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.RenderUpdates()
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def numero_de_ondas(self) -> int:
        return self.__numero_de_ondas

    @property
    def lista_de_inimigos(self) -> list:
        return self.__lista_de_inimigos

    @property
    def background_sprites(self) -> pygame.sprite.Group:
        return self.__background_sprites
    @property
    def tilemap(self) -> list:
        return self.__tilemap

    @property
    def spriteCaixa(self) -> SpritesFlyweight:
        return self.__spriteCaixa

    @property
    def spriteChao(self) -> SpritesFlyweight:
        return self.__spriteChao

    def start_new_round(self):
        map_var = ["BBBBBBBBBBBBBBBBBBBB",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B...P..............B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "B..................B",
                      "BBBBBBBBBBBBBBBBBBBB",
]
        self.change_map(map_var)
        return self.all_sprites


    def change_map(self, new_map_list):
        #self.sprite_blocks.empty()
        #self.background_sprites.empty()
        for i, row in enumerate(new_map_list):
            for j, column in enumerate(row):
                if column == "B":
                    block = Bloco(j, i, self.spriteCaixa.spriteAddress)
                    self.sprite_blocks.add(block)
                elif column == '.':
                    terrain = Terreno(j,i, self.spriteChao.spriteAddress)
                    self.background_sprites.add(terrain)
        return [self.background_sprites, self.sprite_blocks]

    def draw_map(self, spriteGroupsToDraw, surface):
        for i in spriteGroupsToDraw:
            i.draw(surface)
