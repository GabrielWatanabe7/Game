import pygame
from consty import *

GROUND_Y = HEIGHT - 20

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.run = [
            pygame.transform.scale(pygame.image.load("assets/Run__000.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("assets/Run__001.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("assets/Run__002.png").convert_alpha(), (100,100))
        ]

        self.fly = pygame.transform.scale(pygame.image.load("assets/Fly.png").convert_alpha(), (100,100))
        self.fall = pygame.transform.scale(pygame.image.load("assets/Fall.png").convert_alpha(), (100,100))

        self.image = self.run[0]

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.bottom = GROUND_Y

        self.frame = 0

        self.velocity_y = 0
        self.gravity = 1
        self.jump_force = -18
        self.speed = 6

    def update(self):

        keys = pygame.key.get_pressed()

        # movimento lateral
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # pulo
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_Y:
            self.velocity_y = self.jump_force

        # gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # limitar no chão
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity_y = 0

        # animação
        if self.rect.bottom >= GROUND_Y:
            self.frame += 0.2
            if self.frame >= len(self.run):
                self.frame = 0
            self.image = self.run[int(self.frame)]
        else:
            if self.velocity_y < 0:
                self.image = self.fly
            else:
                self.image = self.fall