import pygame as pg
from pong import field as fl
from pong import ball as ba
from pong import players as pl


def main():
    speed = 13
    ball = ba.Ball((0, 0), (0.47, speed))

    player_sprites = pg.sprite.RenderPlain((pl.player1, pl.player2))
    ball_sprite = pg.sprite.RenderPlain(ball)

    fl.Field.screen.blit(fl.Field.background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()
    while 1:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    pl.player1.move_up()
                if event.key == pg.K_z:
                    pl.player1.move_down()
                if event.key == pg.K_UP:
                    pl.player2.move_up()
                if event.key == pg.K_DOWN:
                    pl.player2.move_down()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_a or event.key == pg.K_z:
                    pl.player1.move_pos = [0, 0]
                    pl.player1.state = "still"
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    pl.player2.move_pos = [0, 0]
                    pl.player2.state = "still"

        fl.Field.screen.blit(fl.Field.background, ball.rect, ball.rect)
        fl.Field.screen.blit(fl.Field.background, pl.player1.rect, pl.player1.rect)
        fl.Field.screen.blit(fl.Field.background, pl.player2.rect, pl.player2.rect)

        ball_sprite.update()
        player_sprites.update()
        ball_sprite.draw(fl.Field.screen)
        player_sprites.draw(fl.Field.screen)
        pg.display.flip()


if __name__ == '__main__': main()
