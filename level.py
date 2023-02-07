import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite creation
        self.map_creation()

    def map_creation(self):
        for row_index,row in enumerate(WORLD_MAP):
            for collumn_index, collumn in enumerate(row):
                x = collumn_index * TILESIZE
                y = row_index * TILESIZE
                if collumn == 'x':
                    Tile((x,y),[self.visible_sprites])
                if collumn == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                    

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
