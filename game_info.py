import pygame
import sys



class GameInfo:
    def __init__(self):
        pass

    def start(self):
        pygame.init()

        screen = pygame.display.set_mode((1200, 800))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


