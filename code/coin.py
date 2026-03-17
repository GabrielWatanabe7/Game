import pygame
from consty import *

class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("assets/goldCoin9.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,60))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= GAME_SPEED
