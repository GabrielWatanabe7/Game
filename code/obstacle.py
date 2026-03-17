import pygame
from consty import *

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()

        self.image = pygame.image.load("assets/Box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - 120

    def update(self):
        self.rect.x -= GAME_SPEED