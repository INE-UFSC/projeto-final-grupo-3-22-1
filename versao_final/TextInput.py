import pygame

pygame.init()

class TextInput():

    def __init__(self, pos_x, pos_y, largura, altura, texto=''):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__largura = largura
        self.__altura = altura
        self.__texto = texto
        self.__rect = pygame.Rect(pos_x, pos_y, largura, altura)
        self.__cor = (0,49,83)
        self.__font = pygame.font.Font(f"fonts/alterebro-pixel-font.ttf", 32)
        self.__texto_render = self.font.render(self.texto, True, self.cor)
        self.__ativo = False

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def rect(self):
        return self.__rect

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def font(self):
        return self.__font

    @property
    def texto_render(self):
        return self.__texto_render

    @texto_render.setter
    def texto_render(self, texto_render):
        self.__texto_render = texto_render

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.ativo = True
                self.texto = ''
                self.texto_render = self.font.render(self.texto, True, self.cor)
            else:
                self.ativo = False
            self.cor = (60,23,82) if self.ativo else (0,49,83)

        if event.type == pygame.KEYDOWN:
            if self.ativo:
                if event.key == pygame.K_RETURN:
                    print(self.texto) #salvar em uma variável ao invés de printar
                    self.texto = ''
                    import app
                elif event.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    if len(self.texto) < 20:
                        self.texto += event.unicode
                self.texto_render = self.font.render(self.texto, True, self.cor)

    def desenhar(self, screen):
        screen.blit(self.texto_render, (self.pos_x+10, self.pos_y+2))
        pygame.draw.rect(screen, self.cor, self.rect, 4)
