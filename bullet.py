from game_object import *
from enemy import *
from shuttle import *


class Bullet(GameObject):
    def __init__(self, sender_class, x, y, v, width, height):
        super().__init__(x, y, v, width, height)
        self.sender_class = sender_class
        self.targets = []
        self.set_targets()

    def move(self):
        # print("moves")
        if not self.is_alive:
            return
        self.y -= self.velocity

    def try_hit(self, another_game_object):
        for target in self.targets:
            if isinstance(another_game_object, target) and self.is_intersected_with(another_game_object):
                print("hit")
                another_game_object.get_hit()
                self.die()

    def set_targets(self):
        if self.sender_class == Shuttle:
            self.targets = [Enemy]

