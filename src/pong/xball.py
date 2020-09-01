import pygame as py
import random as rn


class Ball(py.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        black = (0, 0, 0)

        # Pass in the color of the ball, its width and height
        # Set the background color and set it to be transparent
        self.image = py.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the ball
        py.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [rn.randint(4, 8), rn.randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = rn.randint(-8, 8)
