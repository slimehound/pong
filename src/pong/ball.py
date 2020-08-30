import pygame as pg
import numpy as np
import players as pl


class Ball(pg.sprite.Sprite):
    def __init__(self, vector, new_pos):
        pg.sprite.Sprite.__init__(self)
        self.rect = new_pos
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

    def update(self):
        new_pos = self.calc_new_pos(self.rect, self.vector)
        (angle, z) = self.vector

        if not self.area.contains(new_pos):
            tl = not self.area.collidepoint(new_pos.topleft)
            tr = not self.area.collidepoint(new_pos.topright)
            bl = not self.area.collidepoint(new_pos.bottomleft)
            br = not self.area.collidepoint(new_pos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                angle = np.pi - angle
            if tr and br:
                angle = np.pi - angle
        else:
            pl.player1.rect.inflate(-3, -3)
            pl.player2.rect.inflate(-3, -3)
            if self.rect.colliderect(pl.player1.rect) == 1 and not self.hit:
                angle = np.pi - angle
                self.hit = not self.hit
            elif self.rect.colliderect(pl.player2.rect) == 1 and not self.hit:
                angle = np.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle, z)

    @staticmethod
    def calc_new_pos(rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*np.cos(angle), z*np.sin(angle))
        return rect.move(dx, dy)
