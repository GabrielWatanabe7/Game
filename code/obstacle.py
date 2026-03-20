import pygame
import random
from consty import *

# Spawn control
last_obstacle_x = WIDTH
MIN_DISTANCE = 250
MAX_DISTANCE = 400

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()

        self.image = pygame.image.load("assets/Box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - 120

    def update(self):
        self.rect.x -= GAME_SPEED


# Function to spawn obstacle with proper spacing
def spawn_obstacle(group):
    global last_obstacle_x

    new_x = last_obstacle_x + random.randint(MIN_DISTANCE, MAX_DISTANCE)

    obstacle = Obstacle(new_x)
    group.add(obstacle)

    last_obstacle_x = new_x