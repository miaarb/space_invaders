import pygame
import sys
from tank import *


def game_loop():
    pygame.init()
    screen_width = 1200
    screen_height = 700
    tank_size_x = 100
    tank_size_y = 50
    margin = 50
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    tank_x = margin
    tank_y = screen_height - margin - tank_size_y
    velocity = 10
    tank_frame = pygame.Rect(tank_x, tank_y, tank_size_x, tank_size_y)
    tank = Tank(tank_x, tank_y, velocity)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 0, 0), tank_frame, 0)
    while True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tank.is_moving_left = True
                if event.key == pygame.K_RIGHT:
                    tank.is_moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tank.is_moving_left = False
                if event.key == pygame.K_RIGHT:
                    tank.is_moving_right = False
        if tank.x < 0:
            tank.is_moving_left = False
        if tank.x + tank_size_x > screen_width:
            tank.is_moving_right = False
        tank.move()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 0, 0), (tank.x, tank.y, tank_size_x, tank_size_y), 0)
        pygame.display.flip()


game_loop()
