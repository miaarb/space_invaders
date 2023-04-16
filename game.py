import pygame
import sys

from game_info import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load(r"images\shuttle.png")
        pygame.display.set_icon(icon)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        # self.shuttle_width = 100
        # self.shuttle_height = 50

        self.shuttle_image = pygame.image.load(r"images\shuttle.png")
        self.shuttle_width = self.shuttle_image.get_width()
        self.shuttle_height = self.shuttle_image.get_height()
        self.shuttle_velocity = 10

        self.margin = 50

        self.bullet_image = pygame.image.load(r"images\bullet.png")
        self.bullet_width = self.bullet_image.get_width()
        self.bullet_height = self.bullet_image.get_height()
        self.bullet_velocity = 20

        self.enemy_image = pygame.image.load(r"images\cat_enemy.png")
        self.enemy_width = self.enemy_image.get_width()
        self.enemy_height = self.enemy_image.get_height()
        self.enemy_velocity = 3

        self.game_info = GameInfo(self.screen_width, self.screen_height,
                                  self.shuttle_width, self.shuttle_height, self.shuttle_velocity,
                                  self.bullet_width, self.bullet_height, self.bullet_velocity,
                                  self.enemy_width, self.enemy_height, self.enemy_velocity)
        self.shuttle = self.game_info.shuttle

        self.rjuman_image = pygame.image.load(r"images/rjuman.png")

        self.game_info.start_new_level()
        # self.enemy_matrix_width = 4
        # self.enemy_matrix_height = 3
        # self.game_info.fill_enemy_matrix(self.enemy_matrix_width, self.enemy_matrix_height)

    # @classmethod
    # def new_base_game(cls):
    #     pass
    #     # return cls()

    def game_loop(self):
        while True:
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.process_game_keydown(event.key)
                if event.type == pygame.KEYUP:
                    self.process_game_keyup(event.key)

            self.game_info.update()
            self.draw()
            if self.game_info.is_level_completed:
                self.level_completed()
            elif not self.game_info.is_player_alive:
                self.show_player_died()
            pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_shuttle()
        self.draw_bullets()
        self.draw_enemies()
        self.draw_score()
        # pygame.display.flip()

    def level_completed(self):
        self.screen.blit(self.rjuman_image, (self.screen_width // 2 - self.rjuman_image.get_width() // 2,
                                             self.screen_height // 2 - self.rjuman_image.get_height() * 5//8))
        pygame.display.flip()
        pygame.time.delay(1500)
        self.game_info.start_new_level()

    def show_player_died(self):
        text = self.font.render(f"You lose. Score: {self.game_info.player_score}", False, (200, 0, 0))
        self.screen.blit(text, (self.screen_width // 2 - text.get_bounding_rect().width // 2,
                                self.screen_height // 2 - text.get_bounding_rect().height))
        # pygame.display.flip()

    def draw_score(self):
        score = self.game_info.player_score
        score_text_surface = self.font.render(str(score), True, (200, 200, 200))
        self.screen.blit(score_text_surface, (0, 0))

    def draw_shuttle(self):
        # pygame.draw.rect(self.screen, (100, 0, 0),
        #                  (self.shuttle.x, self.shuttle.y, self.shuttle.width, self.shuttle.height), 0)
        self.screen.blit(self.shuttle_image, (self.shuttle.x, self.shuttle.y))

    def draw_bullets(self):
        if self.game_info.shuttle_bullets:
            bullet = self.game_info.shuttle_bullets[0]
            if bullet.is_alive:
                # pygame.draw.rect(self.screen, (0, 100, 0), (bullet.x, bullet.y,
                #                                             bullet.width, bullet.height), 0)
                self.screen.blit(self.bullet_image,
                                 (bullet.x, bullet.y, bullet.width, bullet.height))

    def draw_enemies(self):
        for enemy in self.game_info.enemies:
            if enemy.is_alive:
                # pygame.draw.rect(self.screen, (0, 0, 100), (enemy.x, enemy.y, enemy.width, enemy.height))
                self.screen.blit(self.enemy_image, (enemy.x, enemy.y))

    def process_game_keydown(self, key):
        if not self.game_info.is_active:
            return
        if key == pygame.K_LEFT:
            self.shuttle.is_moving_left = True
        if key == pygame.K_RIGHT:
            self.shuttle.is_moving_right = True
        if key == pygame.K_SPACE and not self.game_info.shuttle_bullets:
            self.game_info.shuttle_bullets.append(Bullet(Shuttle,
                                                         self.shuttle.x + self.shuttle.width // 2,
                                                         self.shuttle.y - self.bullet_width + self.bullet_velocity,
                                                         self.bullet_velocity,
                                                         self.bullet_width,
                                                         self.bullet_height))

    def process_game_keyup(self, key):
        if key == pygame.K_LEFT:
            self.shuttle.is_moving_left = False
        if key == pygame.K_RIGHT:
            self.shuttle.is_moving_right = False


# game = Game()
# game.game_loop()
