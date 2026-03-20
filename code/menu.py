import pygame
from consty import *

def draw_text_with_shadow(screen, text, font, color, center_pos):
    shadow = font.render(text, True, (0, 0, 0))
    main = font.render(text, True, color)

    rect = main.get_rect(center=center_pos)
    shadow_rect = shadow.get_rect(center=(center_pos[0]+3, center_pos[1]+3))

    screen.blit(shadow, shadow_rect)
    screen.blit(main, rect)


def menu(screen):

    pygame.mixer.music.load("assets/Menu.mp3.mp3")
    pygame.mixer.music.play(-1)

    font_title = pygame.font.SysFont("Lucida Sans Typewriter", 60)
    font_text = pygame.font.SysFont("Lucida Sans Typewriter", 30)

    menu_bg = pygame.image.load("assets/pre.png")
    menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    while True:

        screen.blit(menu_bg, (0, 0))

        # 🎮 TÍTULO
        draw_text_with_shadow(
            screen, "Coin Rush", font_title, (255, 255, 255),
            (WIDTH // 2, 140)
        )

        # 🎮 CONTROLES
        draw_text_with_shadow(
            screen, "A / D - Move", font_text, (200, 200, 200),
            (WIDTH // 2, 250)
        )

        draw_text_with_shadow(
            screen, "SPACE - Jump", font_text, (200, 200, 200),
            (WIDTH // 2, 290)
        )

        # ✨ TEXTO PISCANDO
        if pygame.time.get_ticks() % 1000 < 500:
            draw_text_with_shadow(
                screen, "Press ENTER to start", font_text, (255, 215, 0),
                (WIDTH // 2, 360)
            )

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return