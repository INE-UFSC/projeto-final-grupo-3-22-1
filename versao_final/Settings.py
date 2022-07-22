from Singleton import Singleton


# classe usada para guardar variáveis de acesso global e de configuração
class Settings(Singleton):
    FPS_VALUE = 20

    largura_tela = 640
    altura_tela = 640
