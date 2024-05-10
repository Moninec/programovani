import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

clock = pygame.time.Clock()

# naše proměnné na obrazovku
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# vytvarime hrace, ktery je obdelník; osa x, y, vyska, sirka
player_surf = pygame.image.load("panacek.png").convert_alpha()
monster_surf = pygame.image.load("monster.png").convert_alpha()
player_x = 100
player_y = 200

monster_x = 300
monster_y = 500

# game loop
while True:
    for event in pygame.event.get():  # kontroluje vsechny eventy, co probehly
        if event.type == pygame.QUIT:  # pokud dojde k události, vypne
            pygame.quit()
            exit()
    # proměnná key, pod ní schováme stisknutou klávesu
    key = pygame.key.get_pressed()
    # pokud stiskneme klávesu A
    if key[pygame.K_a] == True:
        # player.move_ip(-10, 0)´
        player_x -= 10
    elif key[pygame.K_d] == True:
        # player.move_ip(10, 0)
        player_x += 10
    elif key[pygame.K_s] == True:
        # player.move_ip(0, 10)
        player_y += 10
    elif key[pygame.K_w] == True:
        # player.move_ip(0, -10)
        player_y -= 10

    # obarvi obrazovku na černo
    screen.fill((0, 0, 0))

    # nakresli vytvořený obdelník - na obrazovku, červenou barvou, obdelník - hráč
    screen.blit(player_surf, (player_x, player_y))
    screen.blit(monster_surf, (monster_x, monster_y))

    # updatuje vše
    pygame.display.update()

    clock.tick(60)
