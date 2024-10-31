import pygame

from basic.general_game_logic.game_visualization.camera_folder.Camera import Camera
from basic.general_game_logic.game_visualization.support_visualization_components.converting.DrawConverting import \
    DrawConverting


def draw_mouse_game_coordinates(screen: pygame.Surface, camera: Camera, tick_size: int):
    xc, yc = pygame.mouse.get_pos()
    xm, ym = DrawConverting.draw_to_main_coordinates((xc, yc), camera.get_coordinates(), tick_size)

    font = pygame.font.Font(None, 20)
    text = font.render(f"({round(xm, 2)}, {round(ym, 2)})", True, "grey")

    screen.blit(text, (xc, yc + 20))
