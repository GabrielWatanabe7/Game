import pygame
import random
from consty import *

MIN_HEIGHT = 50
MAX_HEIGHT = 120

class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("assets/goldCoin9.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= GAME_SPEED


# Function to spawn coin at reachable height
def spawn_coin(group):
    y = (HEIGHT - 120) - random.randint(MIN_HEIGHT, MAX_HEIGHT)

    coin = Coin(WIDTH, y)
    group.add(coin)