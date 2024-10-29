import pygame


def get_drawing_center_coordinates(parent_surface: pygame.Surface, surface: pygame.Surface):
    width, height = surface.get_size()
    x = (parent_surface.get_width() - width) // 2
    y = (parent_surface.get_height() - height) // 2
    return x, y
