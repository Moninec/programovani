import pygame
from sys import exit

from settings import *
from utility import get_image
from player import Player
from monster import Monster
from level import Level


# from pygame.sprite import _Group

# inicializuje hru - spustíme pygame
pygame.init()

clock = pygame.time.Clock()


# naše proměnné na obrazovku

screen = pygame.display.set_mode((screen_width, screen_height))




# def monster_animation():
#     global monster_surf, monster_index
#     monster_index += 0.1

#     if monster_index > len(monster_walk):
#         monster_index = 0
#     monster_surf = monster_walk[int(monster_index)]








# monster_walk_1 = pygame.image.load("monster.png").convert_alpha()
# monster_walk_2 = pygame.image.load("monster_walk.png").convert_alpha()
# monster_walk = [monster_walk_1, monster_walk_2]

# monster_index = 0

# monster_surf = monster_walk[monster_index]

# monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))

lives = 3


font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 96)

# monster_direction = "Left"
# speed = 5
game_over = False

# invul_time = 0

# immo = False

player = pygame.sprite.GroupSingle()
# player.add(Player())

monsters = pygame.sprite.Group()
# monster = Monster()
# monsters.add(monster)

desk_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

sprites_group = {
    "all": all_sprites,
    "player_group": player,
    "monster_group": monsters,
    "desk_group": desk_group,
    "coin_group": coin_group,
    "powerup_group": powerup_group
}

#vytvoreni sveta
level = Level("tiled/ucebna-final.tmx", screen, sprites_group)
# level.draw_background()


# game loop
while True:
    for event in pygame.event.get():  # kontroluje vsechny eventy, co probehly
        if event.type == pygame.QUIT:  # pokud dojde k události, vypne
            pygame.quit()
            exit()

    

    

    if game_over == False:
        # proměnná key, pod ní schováme stisknutou klávesu
        # screen.fill(("#FFFFFF"))
        level.draw_background()

        text = font.render(f"Lives: {player.sprite.lives} ", False, "#000000")
        screen.blit(text, (1100, 10))


        # pohyb monstra
        # if monster_rect.x <= 0:
        #     monster_direction = "Right"
        # elif monster_rect.x >= screen_width - 50:
        #     monster_direction = "Left"

        # if monster_direction == "Left":
        #     monster_rect.x -= 5
        # if monster_direction == "Right":
        #     monster_rect.x += 5

        # if monster_rect.x <= 0 or monster_rect.x >= screen_width - 50:
        #     speed = -speed
        # monster_rect.x += speed
        # monster_animation()
        # obarvi obrazovku na černo

        # monster.draw(screen)
        # monster.update()

        # player.draw(screen)
        monsters.update()
        player.update()

        player.sprite.invul_time += clock.get_time()

        all_sprites.draw(screen)
        

        
        # nakresli vytvořený obdelník - na obrazovku, červenou barvou, obdelník - hráč
        # screen.blit(player, player_rect)
        # screen.blit(monster_surf, monster_rect)

        # if player.rect.colliderect(monster_rect):
        #     if not immo:
        #         lives -= 1
        #         immo = True
        #         elapsed_time = 0      


        if player.sprite.lives == 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        konec = font2.render(f"Game over!", False, "#FFFFFF")
        screen.blit(konec, (420, 340))

    # updatuje vše
    pygame.display.update()

    clock.tick(60)
