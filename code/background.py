import pygame
from consty import *


class Parallax:

    def __init__(self):

        self.layers = [
            {
                "image": pygame.image.load("assets/Plan 2.png"),
                "speed": 0
            },
            {
                "image": pygame.image.load("assets/Plan 1.png"),
                "speed": 1
            },
            {
                "image": pygame.image.load("assets/Plan 3.png"),
                "speed": 3
            }
        ]

        for layer in self.layers:
            layer["image"] = pygame.transform.scale(layer["image"], (WIDTH, HEIGHT))
            layer["x"] = 0

    def update(self):

        for layer in self.layers:
            layer["x"] -= layer["speed"]

            if layer["x"] <= -WIDTH:
                layer["x"] = 0

    def draw(self, screen):

        for layer in self.layers:
            screen.blit(layer["image"], (layer["x"], 0))
            screen.blit(layer["image"], (layer["x"] + WIDTH, 0))



class Ground(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()

        self.image = pygame.image.load("assets/5.png").convert_alpha()

        # ajustar tamanho do chão para caber na tela
        self.image = pygame.transform.scale(self.image, (WIDTH, 120))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - 120

    def update(self):

        self.rect.x -= GAME_SPEED

        if self.rect.right <= 0:
            self.rect.x = WIDTH