import pygame
from pygame.math import Vector2

class DoctorNPC(pygame.sprite.Sprite):
    def __init__(self, groups, position, surfs):
        super().__init__(groups)

        # images
        self.surfs = surfs
        self.image = surfs["idle down"][1]  # Placeholder surface
        self.rect = self.image.get_frect(center=position)

        # animation
        self.frame_index = 0
        self.idle_max_index = len(surfs["idle down"]) - 1
        self.walk_max_index = len(surfs["down"]) -1
        self.animation_speed = 3.0
        self.is_idle = True
        self.direction = Vector2(0,0)
    def update(self, dt):
        rect_center = self.rect.center
        self.is_idle = True if self.direction.magnitude() == 0 else False
        self.frame_index += self.animation_speed * dt
        if self.is_idle:
            if self.frame_index >= self.idle_max_index:
                self.frame_index = 0
            self.image = self.surfs["idle down"][int(self.frame_index)]
            if self.direction.x > 0:
                self.image = self.surfs["idle right"][int(self.frame_index)]
            elif self.direction.x < 0:
                self.image = self.surfs["idle left"][int(self.frame_index)]
            elif self.direction.y > 0:
                self.image = self.surfs["idle down"][int(self.frame_index)]
            elif self.direction.y < 0:
                self.image = self.surfs["idle up"][int(self.frame_index)]
        else:
            if self.frame_index >= self.idle_max_index:
                self.frame_index = 0
            if self.direction.x > 0:
                self.image = self.surfs["right"][int(self.frame_index)]
            elif self.direction.x < 0:
                self.image = self.surfs["left"][int(self.frame_index)]
            elif self.direction.y > 0:
                self.image = self.surfs["down"][int(self.frame_index)]
            elif self.direction.y < 0:
                self.image = self.surfs["up"][int(self.frame_index)]
        self.rect = self.image.get_frect(center=rect_center)