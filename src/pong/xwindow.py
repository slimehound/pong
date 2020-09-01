import pygame as py


class Window:
    width = 0
    height = 0

    def __init__(self, width, height):
        # Dimension of the screen. Standard is XGA (4:3, 1024x768)
        self.width = width
        self.height = height

        self.screen = py.display.set_mode((width, height))

        # Title of the screen
        py.display.set_caption("Pong")
