import pygame
import sys
from shuttle import *
from bullet import *


class GameInfo:
    def __init__(self, screen_width, screen_height,
                 shuttle_width, shuttle_height, shuttle_velocity,
                 bullet_width, bullet_height, bullet_velocity):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.margin = 50
        self.shuttle = Shuttle(self.margin,
                               screen_height - self.margin - shuttle_height,
                               shuttle_velocity,
                               shuttle_width,
                               shuttle_height)
        self.bullet = None

    def move_all(self):
        self.shuttle.move()
        if self.bullet:
            self.bullet.move()

    def update_shuttle_moving_flags(self):
        if self.shuttle.x < 0:
            self.shuttle.is_moving_left = False
        if self.shuttle.x + self.shuttle.width > self.screen_width:
            self.shuttle.is_moving_right = False

    def update_bullet_broken_flag(self):
        if self.bullet.y < 0 - self.bullet.height:
            self.bullet.is_broken = True
            self.bullet = None







