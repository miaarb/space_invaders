import pygame
import sys
from shuttle import *
from bullet import *
from game_info import *


def game_loop():
    pygame.init()
    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")

    rect_size_x = 100
    rect_size_y = 50
    margin = 50

    velocity = 10
    bullet_size = 10
    bullet_velocity = 20

    game_info = GameInfo(screen_width, screen_height,
                         rect_size_x, rect_size_y, velocity,
                         bullet_size, bullet_size, bullet_velocity)
    shuttle = game_info.shuttle
    # tank_frame = pygame.Rect(shuttle.x, shuttle.y, shuttle.width, shuttle.height)
    bullet = game_info.bullet
    while True:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shuttle.is_moving_left = True
                if event.key == pygame.K_RIGHT:
                    shuttle.is_moving_right = True
                if event.key == pygame.K_SPACE and not game_info.bullet:
                    game_info.bullet = Bullet(shuttle.x + shuttle.width // 2,
                                              shuttle.y - bullet_size + bullet_velocity,
                                              bullet_velocity,
                                              bullet_size, bullet_size)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    shuttle.is_moving_left = False
                if event.key == pygame.K_RIGHT:
                    shuttle.is_moving_right = False

        # if shuttle.x < 0:
        #     shuttle.is_moving_left = False
        # if shuttle.x + rect_size_x > screen_width:
        #     shuttle.is_moving_right = False
        game_info.update()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 0, 0), (shuttle.x, shuttle.y, shuttle.width, shuttle.height), 0)
        if game_info.bullet:
            pygame.draw.rect(screen, (0, 100, 0), (game_info.bullet.x, game_info.bullet.y,
                                                   game_info.bullet.width, game_info.bullet.height), 0)
            # bullet.move()

        pygame.display.flip()


game_loop()
