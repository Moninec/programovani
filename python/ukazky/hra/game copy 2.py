import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

clock = pygame.time.Clock()


# naše proměnné na obrazovku
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

def monster_animation():
    global monster_surf, monster_index
    monster_index += 0.1

    if monster_index > len(monster_walk):
        monster_index = 0
    monster_surf = monster_walk[int(monster_index)]

player_x = 100
player_y = 200

monster_x = 750
monster_y = 500

# vytvarime hrace, ktery je obdelník; osa x, y, vyska, sirka
player_surf = pygame.image.load("panacek.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


monster_walk_1 = pygame.image.load("monster.png").convert_alpha()
monster_walk_2 = pygame.image.load("monster_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]

monster_index = 0

monster_surf = monster_walk[monster_index]

monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))

lives = 3
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 69)

monster_direction = "Left"
# speed = 5
game_over = False

# game loop
while True:
    for event in pygame.event.get():  # kontroluje vsechny eventy, co probehly
        if event.type == pygame.QUIT:  # pokud dojde k události, vypne
            pygame.quit()
            exit()

    if game_over == False:
        # proměnná key, pod ní schováme stisknutou klávesu
        key = pygame.key.get_pressed()
        # pokud stiskneme klávesu A
        if key[pygame.K_a] == True:
            # player.move_ip(-10, 0)´
            player_rect.left -= 10
        elif key[pygame.K_d] == True:
            # player.move_ip(10, 0)
            player_rect.right += 10
        elif key[pygame.K_s] == True:
            # player.move_ip(0, 10)
            player_rect.top += 10
        elif key[pygame.K_w] == True:
            # player.move_ip(0, -10)
            player_rect.bottom -= 10

        # pohyb monstra
        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 50:
            monster_direction = "Left"

        if monster_direction == "Left":
            monster_rect.x -= 5
        if monster_direction == "Right":
            monster_rect.x += 5

        # if monster_rect.x <= 0 or monster_rect.x >= screen_width - 50:
        #     speed = -speed
        # monster_rect.x += speed
        monster_animation()
        # obarvi obrazovku na černo
        screen.fill((0, 0, 0))

        text = font.render(f"Lives: {lives} ", False, "#FFFFFF")
        screen.blit(text, (700, 10))

        # nakresli vytvořený obdelník - na obrazovku, červenou barvou, obdelník - hráč
        screen.blit(player_surf, player_rect)
        screen.blit(monster_surf, monster_rect)

        if player_rect.colliderect(monster_rect):
            lives -= 1
        if lives == 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        konec = font2.render(f"Game over!", False, "#FFFFFF")
        screen.blit(konec, (260, 280))

    # updatuje vše
    pygame.display.update()

    clock.tick(60)
