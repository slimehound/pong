from pong import paddle as pa

global player1
global player2


class Players:
    def __init__(self, player):
        self.player = pa.Paddle("left")
        self.player = pa.Paddle("right")
