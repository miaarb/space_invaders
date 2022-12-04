from game_object import *


class Enemy(GameObject):
    def __init__(self, x, y, v, width, height):
        super().__init__(x, y, v, width, height)
        self.is_alive = True

    def move(self):
        pass

    def die(self):
        self.is_alive = False




