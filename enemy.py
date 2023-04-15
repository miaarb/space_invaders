from game_object import *


class Enemy(GameObject):
    def __init__(self, x, y, v, width, height):
        super().__init__(x, y, v, width, height)
        self.kill_xp = 100

    def move(self, coords_x_y):
        self.x += coords_x_y[0]
        self.y += coords_x_y[1]






