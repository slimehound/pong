import pygame as py
from pong import xwindow as xw
from pong import xpaddle as xp
from pong import xball as xb

py.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Open a new window
my_win = xw.Window(1024, 768)
'''
size = (700, 500)
screen = py.display.set_mode(size)
py.display.set_caption("Pong")
'''

paddleA = xp.Paddle(white, 10, 100)
paddleA.rect.x = 0
paddleA.rect.y = 384

paddleB = xp.Paddle(white, 10, 100)
paddleB.rect.x = 1014
paddleB.rect.y = 384

ball = xb.Ball(white, 10, 10)
ball.rect.x = 507
ball.rect.y = 379


# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = py.sprite.Group()

# Add the car to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The clock will be used to control how fast the screen updates
clock = py.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

running = True
while running:
    for event in py.event.get():  # User did something
        if event.type == py.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop
        elif event.type == py.KEYDOWN:
            if event.key == py.K_x:  # Pressing the x key quits the game
                running = False

    # Moving the paddles when the use uses the "W/S" keys (player A) or the arrow keys (player B)
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        paddleA.move_up(5)
    if keys[py.K_s]:
        paddleA.move_down(5)
    if keys[py.K_UP]:
        paddleB.move_up(5)
    if keys[py.K_DOWN]:
        paddleB.move_down(5)

    # Game logic
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls
    if ball.rect.x >= 1014:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 758:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddles
    if py.sprite.collide_mask(ball, paddleA) or py.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    my_win.screen.fill(black)
    py.draw.line(my_win.screen, white, [512, 0], [512, 768], 5)

    # Sprites drawn
    all_sprites_list.draw(my_win.screen)

    # Display scores:
    font = py.font.Font(None, 74)
    text = font.render(str(scoreA), 1, white)
    my_win.screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, white)
    my_win.screen.blit(text, (774, 10))

    # Update screen
    py.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

py.quit()
