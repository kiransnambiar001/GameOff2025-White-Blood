import pygame, sys
from player import Player
from settings import *
from map import Level

pygame.init()
pygame.font.init()


# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("gmae jamming")
clock = pygame.time.Clock()


# sprite groups
player_group = pygame.sprite.GroupSingle()
level = Level()
# Add player to both the update group and the camera-aware map group so it draws with the same offset.
player = Player((player_group, level.tiles), position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), size=25)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the background
    dt = clock.tick(60)/1000
    keys = pygame.key.get_pressed()
    screen.fill((100, 100, 100))

    player_group.update(dt, keys)

    level.tiles.draw(player.rect)

    # Update the display
    pygame.display.flip()


pygame.quit()