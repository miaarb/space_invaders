from game_object import *


class Bullet(GameObject):
    def __init__(self, x, y, v, width, height):
        super().__init__(x, y, v, width, height)
        self.is_broken = False

    def move(self):
        print("moves")
        if self.is_broken:
            return
        self.y -= self.velocity
