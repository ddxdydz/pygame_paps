import pygame


def create_error_surface(width_px, height_px, color="blue"):
    width_px, height_px = int(width_px), int(height_px)

    error_surface = pygame.Surface((width_px, height_px))
    error_surface.fill(color)

    font = pygame.font.Font(None, min(width_px, height_px))
    text = font.render("?", True, "white")
    error_surface.blit(text, ((width_px - text.width) // 2, ((height_px - text.height) // 2)))

    return error_surface
