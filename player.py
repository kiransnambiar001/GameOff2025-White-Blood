import pygame
from pygame import Vector2
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, position, size):
        if isinstance(groups, pygame.sprite.AbstractGroup):
            super().__init__(groups)
        else:
            super().__init__(*groups)
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))  # Green color for the player
        self.rect = self.image.get_frect(center=position)
        self.speed = 100  # pixels per second
        self.movement = Vector2(0, 0)

    def collisions_check(self, tiles):
        pass

    def update(self, dt, keys):
        self.movement.xy = 0, 0
        if keys[pygame.K_a]:
            self.movement.x = -1
        if keys[pygame.K_d]:
            self.movement.x = 1
        if keys[pygame.K_w]:
            self.movement.y = -1
        if keys[pygame.K_s]:
            self.movement.y = 1

        normalized = self.movement.normalize() if self.movement.length() > 0 else self.movement
        self.rect.center += normalized * self.speed * dt