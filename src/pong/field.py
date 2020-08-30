import pygame as pg


class Field:
    screen = pg.display.set_mode((640, 480))
    pg.display.set_caption('Pong')
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
