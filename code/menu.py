import pygame
from consty import *

def menu(screen):

    pygame.mixer.music.load("assets/Menu.mp3.mp3")
    pygame.mixer.music.play(-1)

    font_title = pygame.font.SysFont("Arial",60)
    font_text = pygame.font.SysFont("Arial",30)

    menu_bg = pygame.image.load("assets/background_03.jpg")
    menu_bg = pygame.transform.scale(menu_bg,(WIDTH,HEIGHT))

    while True:

        screen.blit(menu_bg,(0,0))

        title = font_title.render("RUNNER GAME",True,(255,255,255))
        play = font_text.render("Press ENTER to start",True,(255,255,0))

        controls1 = font_text.render("A / D - Move",True,(255,255,255))
        controls2 = font_text.render("SPACE - Fly",True,(255,255,255))

        title_rect = title.get_rect(center=(WIDTH/2,150))
        play_rect = play.get_rect(center=(WIDTH/2,350))
        c1_rect = controls1.get_rect(center=(WIDTH/2,250))
        c2_rect = controls2.get_rect(center=(WIDTH/2,290))

        screen.blit(title,title_rect)
        screen.blit(play,play_rect)
        screen.blit(controls1,c1_rect)
        screen.blit(controls2,c2_rect)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return