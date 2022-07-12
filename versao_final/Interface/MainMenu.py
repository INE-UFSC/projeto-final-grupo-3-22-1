import pygame as pg
from Interface import Interface

class MainMenu(Interface):

    def __init__(p_mouse):
        p_mouse = pg.mouse.get_pos()