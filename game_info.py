import pygame
import sys
from shuttle import *
from bullet import *
from game_object import *
from enemy_destination import *


class GameInfo:
    def __init__(self, screen_width, screen_height,
                 shuttle_width, shuttle_height, shuttle_velocity,
                 bullet_width, bullet_height, bullet_velocity,
                 enemy_width, enemy_height, enemy_velocity):
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
        self.enemy_velocity = enemy_velocity
        self.enemy_distance = enemy_width // 4
        # self.enemies = [Enemy(200, 300, 0, self.enemy_width, self.enemy_height)]
        self.enemy_matrix_width = 5
        self.enemy_matrix_height = 2
        self.enemy_matrix = [[]]
        self.enemy_upper_bareer = self.margin
        self.enemy_left_bareer = 0
        self.enemy_count = 0
        self.enemy_destination = EnemyDestination.right
        self.player_score = 0
        self.is_player_alive = True
        self.is_level_completed = False
        self.is_active = True

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

    def start_new_level(self):
        self.fill_enemy_matrix(self.enemy_matrix_width, self.enemy_matrix_height, self.enemy_distance)
        self.is_active = True
        self.is_player_alive = True

    def update(self):
        if not self.is_active:
            return
        self.move_all()
        self.update_shuttle_moving_flags()
        self.update_bullet_broken_flag()
        self.check_is_level_completed()
        #     self.new_level()

    def move_all(self):
        # print("move_all")
        self.shuttle.move()
        if self.shuttle_bullets:
            print("bullet moves")
            self.shuttle_bullets[0].move()
        self.move_enemies()

    def move_enemies(self):
        if (self.enemy_destination == EnemyDestination.right
                and self.enemy_matrix[0][-1].x + self.enemy_width >= self.screen_width) \
                or (self.enemy_destination == EnemyDestination.left
                    and self.enemy_matrix[0][0].x <= 0):
            self.change_enemy_destination()
            self.enemy_upper_bareer += self.enemy_height // 2

        if (self.enemy_destination in [EnemyDestination.down_then_left, EnemyDestination.down_then_right]
                and self.enemy_matrix[0][0].y >= self.enemy_upper_bareer):
            self.change_enemy_destination()

        coords = self.get_enemy_move_coords()
        for enemy in self.enemies:
            enemy.move(coords)
            # print(self.enemy_destination )


    def change_enemy_destination(self):
        ordered_destinations = [EnemyDestination.left,
                         EnemyDestination.down_then_right,
                         EnemyDestination.right,
                         EnemyDestination.down_then_left]
        for i in range(len(ordered_destinations)):
            if self.enemy_destination == ordered_destinations[i]:
                print(self.enemy_destination, '-> ', end='')
                self.enemy_destination = ordered_destinations[(i + 1) % len(ordered_destinations)]
                print(self.enemy_destination)
                break

    def get_enemy_move_coords(self):
        if self.enemy_destination == EnemyDestination.left:
            return [-self.enemy_velocity, 0]
        elif self.enemy_destination == EnemyDestination.right:
            return [self.enemy_velocity, 0]
        else:
            return [0, self.enemy_velocity]

    def create_enemy(self, x, y):
        return Enemy(x, y, self.enemy_velocity, self.enemy_width, self.enemy_height)

    def check_is_level_completed(self):
        if self.enemy_count == 0:
            self.is_active = False
            self.is_level_completed = True
        else:
            self.is_level_completed = False

    def update_shuttle_moving_flags(self):
        if self.shuttle.x <= 0:
            self.shuttle.is_moving_left = False
        if self.shuttle.x + self.shuttle.width >= self.screen_width:
            self.shuttle.is_moving_right = False

    def update_bullet_broken_flag(self):
        # print("updating")
        if not self.shuttle_bullets:
            return
        for enemy in self.enemies:
            if not enemy.is_alive:
                continue
            print("check enemy")
            self.shuttle_bullets[0].try_hit(enemy)
            if not enemy.is_alive:
                self.player_score += enemy.kill_xp
                self.enemy_count -= 1
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
        self.enemy_count = width * height












