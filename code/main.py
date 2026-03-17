import pygame
import random

from consty import *
from player import Player
from obstacle import Obstacle
from coin import Coin
from menu import menu
from background import Parallax, Ground
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Runner Game")

clock = pygame.time.Clock()

menu(screen)

pygame.mixer.music.load("assets/Level1.mp3.mp3")
pygame.mixer.music.play(-1)

parallax = Parallax()

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()

ground1 = Ground(0)
ground2 = Ground(WIDTH)

groundGroup.add(ground1, ground2)

obstacleGroup = pygame.sprite.Group()
coinGroup = pygame.sprite.Group()

score = 0
font = pygame.font.SysFont("Arial",30)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    parallax.update()
    parallax.draw(screen)

    playerGroup.update()
    groundGroup.update()
    obstacleGroup.update()
    coinGroup.update()

    if random.randint(0,120) == 1:
        obstacle = Obstacle(WIDTH + 50)
        obstacleGroup.add(obstacle)

    if random.randint(0,90) == 1:
        coin = Coin(WIDTH + 50, random.randint(200,400))
        coinGroup.add(coin)

    if pygame.sprite.spritecollide(player, coinGroup, True):
        score += 1

    if pygame.sprite.spritecollide(player, obstacleGroup, False):
        running = False

    playerGroup.draw(screen)
    groundGroup.draw(screen)
    obstacleGroup.draw(screen)
    coinGroup.draw(screen)

    score_text = font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(score_text,(20,20))

    pygame.display.update()

pygame.quit()