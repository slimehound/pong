import pygame as pg


class Paddle(pg.sprite.Sprite):
    def __init__(self, side, new_pos):
        pg.sprite.Sprite.__init__(self)
        self.rect = new_pos
        self.move_pos = [0, 0]
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.re_init()

    def re_init(self):
        self.state = "still"
        if self.side == "left":
            self.rect.mid_left = self.area.midleft
        elif self.side == "right":
            self.rect.mid_right = self.area.midright

    def update(self):
        new_pos = self.rect.move(self.move_pos)
        if self.area.contains(new_pos):
            pass
        pg.event.pump()

    def move_up(self):
        self.move_pos[1] = self.move_pos[1] - self.speed
        self.state = "move_up"

    def move_down(self):
        self.move_pos[1] = self.move_pos[1] + self.speed
        self.state = "move_down"
