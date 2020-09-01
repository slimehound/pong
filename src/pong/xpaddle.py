import pygame as py


class Paddle(py.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        black = (0, 0, 0)

        # Pass in the color of the paddle, and its x and y position, width and height
        # Set the background color and set it to be transparent
        self.image = py.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the paddle
        py.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels

        # Check that you are not going too far off the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels

        # Check that you are not going too far off the screen
        if self.rect.y > 668:
            self.rect.y = 668
