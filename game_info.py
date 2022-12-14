import pygame
import sys
from shuttle import *
from bullet import *
from game_object import *


class GameInfo:
    def __init__(self, screen_width, screen_height,
                 shuttle_width, shuttle_height, shuttle_velocity,
                 bullet_width, bullet_height, bullet_velocity,
                 enemy_width, enemy_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.margin = 50
        self.shuttle = Shuttle(self.margin,
                               screen_height - self.margin - shuttle_height,
                               shuttle_velocity,
                               shuttle_width,
                               shuttle_height)
        self.shuttle_bullets = []
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_velocity = bullet_velocity
        self.screen = GameObject(0, 0, 0, screen_width, screen_height)
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.enemy_velocity = 0
        # self.enemies = [Enemy(200, 300, 0, self.enemy_width, self.enemy_height)]
        self.enemy_matrix = [[]]
        self.enemy_upper_bareer = self.margin
        self.enemy_left_bareer = 0
        self.player_score = 0

    # @classmethod
    # def new_standard_game_info(cls, screen_width, screen_height):
    #     return GameInfo(screen_width,
    #                     screen_height,
    #                     shuttle_width=)

    @property
    def enemies(self):
        res = []
        for enemies_row in self.enemy_matrix:
            res += enemies_row
        return res

    def update(self):
        self.move_all()
        self.update_shuttle_moving_flags()
        self.update_bullet_broken_flag()

    def move_all(self):
        # print("move_all")
        self.shuttle.move()
        if self.shuttle_bullets:
            print("bullet moves")
            self.shuttle_bullets[0].move()

    def create_enemy(self, x, y):
        return Enemy(x, y, self.enemy_velocity, self.enemy_width, self.enemy_height)

    def update_shuttle_moving_flags(self):
        if self.shuttle.x < 0:
            self.shuttle.is_moving_left = False
        if self.shuttle.x + self.shuttle.width > self.screen_width:
            self.shuttle.is_moving_right = False

    def update_bullet_broken_flag(self):
        # print("updating")
        if not self.shuttle_bullets:
            return
        for enemy in self.enemies:
            if not enemy.is_alive:
                continue
            print("check enemy")
            hit_enemy = self.shuttle_bullets[0].try_hit(enemy)
            if not enemy.is_alive:
                self.player_score += enemy.kill_xp
        if self.shuttle_bullets[0].y < - self.shuttle_bullets[0].height:
            self.shuttle_bullets[0].die()
        if not self.shuttle_bullets[0].is_alive:
            self.shuttle_bullets.pop(0)

    def fill_enemy_matrix(self, width, height, distance=15):
        x0 = self.enemy_left_bareer
        y0 = self.enemy_upper_bareer
        self.enemy_matrix = \
            [[self.create_enemy(x0 + (self.enemy_width + distance) * j, y0 + (self.enemy_height + distance) * i)
              for j in range(width)]
             for i in range(height)]












