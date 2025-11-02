from settings import *
import pygame
from groups import MapSprites
from pytmx import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, image, position):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

class Level:
    def __init__(self):
        # Create sprite groups
        self.tiles = MapSprites()
        
        # Load the map
        self.load_map()

    def load_map(self):
        map = load_pygame(hospital_path)

        for layer in map.visible_layers:
            for x, y, gid in layer:
                tile_image = map.get_tile_image_by_gid(gid)
                if tile_image:
                    tile = Tile((self.tiles), tile_image, (x * TILE_SIZE, y * TILE_SIZE))