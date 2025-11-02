import pygame
from settings import *

class MapSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def draw(self, target):
        if hasattr(target, "center"):
            target_pos = pygame.math.Vector2(target.center)
        else:
            target_pos = pygame.math.Vector2(target)

        self.offset.x = target_pos.x - WINDOW_WIDTH // 2
        self.offset.y = target_pos.y - WINDOW_HEIGHT // 2

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)