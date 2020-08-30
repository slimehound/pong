import pygame as pg
import os


class LoadPNG:
    def __init__(self,name):
        fullname = os.path.join('data', self.name)
        try:
            image = pg.image.load(fullname)
            if image.get_alpha is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except Exception:
            pass

        # return image, image.get_rect()
