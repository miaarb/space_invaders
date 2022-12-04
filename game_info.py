import pygame
import sys
from shuttle import *
from bullet import *
from game_object import *


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
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_velocity = bullet_velocity
        self.screen = GameObject(0,0,0,screen_width, screen_height)
        self.enemies = []

    # @classmethod
    # def new_standard_game_info(cls, screen_width, screen_height):
    #     return GameInfo(screen_width,
    #                     screen_height,
    #                     shuttle_width=)

    def update(self):
        self.move_all()
        self.update_shuttle_moving_flags()
        self.update_bullet_broken_flag()

    def move_all(self):
        print("move_all")
        self.shuttle.move()
        if self.bullet:
            print("bullet moves")
            self.bullet.move()

    def update_shuttle_moving_flags(self):
        if self.shuttle.x < 0:
            self.shuttle.is_moving_left = False
        if self.shuttle.x + self.shuttle.width > self.screen_width:
            self.shuttle.is_moving_right = False

    def update_bullet_broken_flag(self):
        if self.bullet and self.bullet.y < - self.bullet.height:
            self.bullet.is_broken = True
            self.bullet = None









