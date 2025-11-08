import pygame
from pygame import Vector2
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, position, size, old_man_sprites):
        if isinstance(groups, (list, tuple, set)):
            super().__init__(*groups)
        else:
            super().__init__(groups)
        self.image = old_man_sprites["down"][0]
        self.rect = self.image.get_frect(center=position)
        self.hitbox = self.rect.inflate(-4, -32)
        self.hitbox.midbottom = self.rect.midbottom
        self.speed = 100  # pixels per second
        self.movement = Vector2(0, 0)
        self.old_man_sprites = old_man_sprites
        self.frame_index = 0
        self.animation_speed = 2.5

    def animate(self, dt, movement):
        if movement.x > 0:
            direction = "right"
        elif movement.x < 0:
            direction = "left"
        elif movement.y > 0:
            direction = "down"
        elif movement.y < 0:
            direction = "up"
        else:
            direction = None

        if direction:
            if self.frame_index >= len(self.old_man_sprites[direction])-1:
                self.frame_index = 0
            self.frame_index += self.animation_speed * dt
            self.image = self.old_man_sprites[direction][int(self.frame_index)]
            self.rect = self.image.get_frect(center=self.rect.center)
            self.hitbox = self.rect.inflate(-4, -32)
            self.hitbox.midbottom = self.rect.midbottom

    def collisions_check(self, tiles, direction):
        for tile in tiles:
            if self.hitbox.colliderect(tile.rect):
                if direction == 1: # x-axis
                    if self.movement.x > 0:  # Moving right
                        self.hitbox.right = tile.rect.left
                    if self.movement.x < 0:  # Moving left
                        self.hitbox.left = tile.rect.right
                if direction == 2: # y-axis
                    if self.movement.y > 0:  # Moving down
                        self.hitbox.bottom = tile.rect.top
                    if self.movement.y < 0:  # Moving up
                        self.hitbox.top = tile.rect.bottom

    def update(self, dt, keys, tiles):
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

        self.hitbox.centerx += normalized.x * self.speed * dt
        self.collisions_check(tiles, 1)  # Check x-axis collisions
        self.hitbox.centery += normalized.y * self.speed * dt
        self.collisions_check(tiles, 2)  # Check y-axis collisions
        self.rect.midbottom = self.hitbox.midbottom
        self.animate(dt, self.movement)