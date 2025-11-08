import pygame, sys
from sprites import *
from player import Player
from settings import *
from map import Level
from helper import *
from pathlib import Path

pygame.init()
pygame.font.init()


# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("gmae jamming")
clock = pygame.time.Clock()


# imports
old_man_sprites = {} 
old_man_sprites["down"] = import_spritesheet(Path("assets", "images", "old_man", "old_man_down.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
old_man_sprites["up"] = import_spritesheet(Path("assets", "images", "old_man", "old_man_up.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
old_man_sprites["left"] = import_spritesheet(Path("assets", "images", "old_man", "old_man_left.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
old_man_sprites["right"] = import_spritesheet(Path("assets", "images", "old_man", "old_man_right.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))

doctor_sprites = {}
doctor_sprites["down"] = import_spritesheet(Path("assets", "images", "doctor", "doctor_down.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
doctor_sprites["up"] = import_spritesheet(Path("assets", "images", "doctor", "doctor_up.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
doctor_sprites["left"] = import_spritesheet(Path("assets", "images", "doctor", "doctor_left.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))
doctor_sprites["right"] = import_spritesheet(Path("assets", "images", "doctor", "doctor_right.png"), (32,32), (0,0), scale_by=2, trim=(5,4,5,0))

# sprite groups
player_group = pygame.sprite.GroupSingle()
doctor_group = pygame.sprite.GroupSingle()
level = Level()
# Add player to both the update group and the camera-aware map group so it draws with the same offset.
player = Player(groups=(player_group, level.tiles), position=(156, 464), size=25, old_man_sprites=old_man_sprites)
doctor = DoctorNPC(groups=(doctor_group, level.tiles), position=(156, 464), surfs=old_man_sprites)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the background
    dt = clock.tick(60)/1000
    keys = pygame.key.get_pressed()
    screen.fill((125, 150, 48))

    player_group.update(dt, keys, level.collision_tiles)

    level.tiles.draw(player.rect)

    # Update the display
    pygame.display.flip()


pygame.quit()