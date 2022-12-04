from game_object import *
from enemy import *


class Bullet(GameObject):
    def __init__(self, x, y, v, width, height):
        super().__init__(x, y, v, width, height)
        self.is_broken = False

    def move(self):
        print("moves")
        if self.is_broken:
            return
        self.y -= self.velocity

    def try_hit(self, another_game_object):
        if another_game_object is Enemy and self.is_intersected_with(another_game_object):
            another_game_object.die()

