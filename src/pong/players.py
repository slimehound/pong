import Paddle from paddle


class Players:
    def __init__(self, player):
        player1 = self.player = Paddle("left")
        player2 = self.player = Paddle("right")
