import pygame
from settings import *

def import_spritesheet(path, sprite_dimensions=(TILE_SIZE, TILE_SIZE), start_offset=(0, 0), scale_by=None, trim=(0, 0, 0, 0)):
    """Imports a spritesheet and returns a list of individual sprite surfaces.

    `trim` is ordered (left, top, right, bottom) and is applied to every sprite frame.
    """
    sheet = pygame.image.load(path).convert_alpha()
    sprites = []

    sprite_width, sprite_height = sprite_dimensions
    offset_x, offset_y = start_offset
    trim_left, trim_top, trim_right, trim_bottom = trim

    sheet_width, sheet_height = sheet.get_width(), sheet.get_height()
    usable_width = sheet_width - offset_x
    usable_height = sheet_height - offset_y

    if usable_width <= 0 or usable_height <= 0:
        return sprites

    columns = usable_width // sprite_width
    rows = usable_height // sprite_height

    for row in range(rows):
        for col in range(columns):
            x = offset_x + col * sprite_width
            y = offset_y + row * sprite_height
            cropped_x = x + trim_left
            cropped_y = y + trim_top
            cropped_width = sprite_width - (trim_left + trim_right)
            cropped_height = sprite_height - (trim_top + trim_bottom)

            if cropped_width <= 0 or cropped_height <= 0:
                continue

            rect = pygame.Rect(cropped_x, cropped_y, cropped_width, cropped_height)

            if not sheet.get_rect().contains(rect):
                continue

            sprite = sheet.subsurface(rect).copy()
            if scale_by:
                sprite = pygame.transform.scale_by(sprite, scale_by)
            sprites.append(sprite)

    return sprites