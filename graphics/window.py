import pygame
from sys import exit


class Window:
    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def update(self, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        grid.draw()

        pygame.display.update()
