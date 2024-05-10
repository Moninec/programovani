import pygame
from utility import get_image
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, sprites_group):
        super().__init__()
        self.position = position
        # self.
        self.index = 0
        self.spritesheet = pygame.image.load("assets/player/man_brownhair_run.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.position))

        self.score = 0
        self.lives = 3
        self.invul = False
        self.invul_time = 0
        self.speed = 10
        for key, group in sprites_group.items():
            setattr(self, key, group)

    def animation(self, direction):
        frame_count = 4
        
        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0
        
        self.image = get_image(self.spritesheet, int(self.index), direction, 15, 16, 3)

     

    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            # player.move_ip(-10, 0)
            dx -= self.speed
            self.animation(2)
        elif key[pygame.K_d] == True:
            # player.move_ip(10, 0)
            dx += self.speed
            self.animation(3)
        elif key[pygame.K_s] == True:
            # player.move_ip(0, 10)
            dy += self.speed
            self.animation(0)
        elif key[pygame.K_w] == True:
            # player.move_ip(0, -10)
            dy -= self.speed
            self.animation(1)

        self.rect.x += dx
        self.rect.y += dy

        for desk in pygame.sprite.spritecollide(self, self.desk_group, False):
            #pohyb doprava
            if dx > 0:
                self.rect.right = desk.rect.left
            
            #pohyb doleva
            if dx < 0:
                self.rect.left = desk.rect.right

            if dy > 0:
                self.rect.bottom = desk.rect.top

            if dy < 0:
                self.rect.top = desk.rect.bottom



        if self.rect.x < 0:
            self.rect.x = screen_width - 10
        elif self.rect.x > screen_width:
            self.rect.x = 10

        if self.rect.y < 0:
            self.rect.y = screen_width - 10
        elif self.rect.y > screen_width:
            self.rect.y = 10

        
        if pygame.sprite.spritecollide(self, self.monster_group, False):
            
            if not self.invul:
                print("Ahoooooooj")
                self.lives -= 1
                self.invul = True
                self.invul_time = 0 
                self.speed = 20 
        
        if self.invul_time > 1000:
            self.invul = False
            self.speed = 10

        if pygame.sprite.spritecollide(self, self.coin_group, True): #True = zabit nebo nezabit
            self.score += 1

        if pygame.sprite.spritecollide(self, self.powerup_group, True):
            self.lives += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
  
