import pygame
from items import Desk, Coin, PowerUp
from pytmx.util_pygame import load_pygame
from monster import Monster
from player import Player

class Level:
    def __init__(self, level_data, screen, sprites_group):
        # self.path = path
        self.data = load_pygame(level_data)
        self.ground = self.data.get_layer_by_name("ground") #tak jak je to pojmenované v souboru

        self.sprites_group = sprites_group

        for layer in self.data.visible_layers:
            setattr(self, layer.name, self.data.get_layer_by_name(layer.name))

        for key, group in sprites_group.items():
            setattr(self, key, group)

        self.background = pygame.Surface(
            (
            self.data.width * self.data.tilewidth,
            self.data.height * self.data.tileheight
            )
            )
        self.screen = screen

        self.init_items()

        # self.draw_background()
    
    def draw_background(self):
        for x, y, image in self.ground.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0,0))

    def init_items(self):
        self.create_items(self.furniture, Desk, self.desk_group)
        self.create_items(self.spawn_coins, Coin, self.coin_group)
        self.create_items(self.spawn_powerups, PowerUp, self.powerup_group)
        self.create_monsters(self.spawn_enemies_h, self.monster_group)
        self.create_player(self.spawn_player, self.player_group)
    

    def create_items(self, layer, item_class, group):
        for item in layer:
            new_item = item_class(item.image, item.width, item.height, (item.x, item.y))
            group.add(new_item)
            self.all.add(new_item)

    def create_monsters(self, layer, group):
        for monster in layer:
            new_monster = Monster((monster.x, monster.y))
            group.add(new_monster)
            self.all.add(new_monster)

    def create_player(self, layer, group):
        for player in layer:
            new_player = Player((player.x, player.y), self.sprites_group)
            group.add(new_player)
            self.all.add(new_player)


# level = Level("../assets/tiled/ucebna2.tmx")
# level.draw_background()
