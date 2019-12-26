import pygame
from sys import exit


class Window:
    """
    Window class for rendering the maze solving.
    Wraps the pygame screen with a simple update method.
    """

    def __init__(self, width: int, height: int, title: str):
        """
        Initialises pygame and the screen
        
        Arguments:
            width {int} -- screen width in pixels
            height {int} -- screen height in pixels
            title {str} -- window title
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def update(self):
        """
        Updates the pygame window or exits if the window
        is closed
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
