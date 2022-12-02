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

    tank_x = margin
    tank_y = screen_height - margin - rect_size_y
    velocity = 10
    tank_frame = pygame.Rect(tank_x, tank_y, rect_size_x, rect_size_y)
    shuttle = Shuttle(tank_x, tank_y, velocity, rect_size_x, rect_size_y)
    bullet = None
    bullet_size = 10
    bullet_velocity = 30
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 0, 0), tank_frame, 0)
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
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(shuttle.x + rect_size_x // 2, shuttle.y - bullet_size, bullet_velocity,
                                    bullet_size, bullet_size)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    shuttle.is_moving_left = False
                if event.key == pygame.K_RIGHT:
                    shuttle.is_moving_right = False

        if shuttle.x < 0:
            shuttle.is_moving_left = False
        if shuttle.x + rect_size_x > screen_width:
            shuttle.is_moving_right = False
        shuttle.move()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 0, 0), (shuttle.x, shuttle.y, rect_size_x, rect_size_y), 0)
        if bullet:
            pygame.draw.rect(screen, (0, 100, 0), (bullet.x, bullet.y, bullet_size, bullet_size), 0)
            bullet.move()

        pygame.display.flip()


game_loop()
