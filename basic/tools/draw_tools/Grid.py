import pygame

from basic.general_game_logic.game_visualization.camera_folder.Camera import Camera
from basic.general_game_logic.game_visualization.support_visualization_components.converting.DrawConverting import \
    DrawConverting

AXIS_COLOR = (200, 200, 200)
GRID_COLOR = (60, 60, 60)
TEXT_COLOR = "grey"


class Grid:
    @staticmethod
    def draw_coordinates(screen: pygame.Surface, camera: Camera, one_tick_to_px: int,
                         main_coordinates: [float, float], color=TEXT_COLOR, draw_x=True, draw_y=True):
        xm, ym = main_coordinates

        font = pygame.font.Font(None, 20)
        if draw_x and draw_y:
            text = font.render(f"({round(xm, 2)}, {round(ym, 2)})", True, color)
        elif draw_x:
            text = font.render(f"{round(xm, 2)}", True, color)
        else:
            text = font.render(f"{round(ym, 2)}", True, color)

        screen.blit(text, DrawConverting.main_to_draw_coordinates(
            main_coordinates, camera.get_coordinates(), one_tick_to_px))

    @staticmethod
    def draw_vertical_screen_line(screen: pygame.Surface, camera: Camera, one_tick_to_px: int, main_x: float, color):
        _, camera_y = camera.get_coordinates()
        _, camera_height = camera.get_obj_size()
        pygame.draw.line(
            screen, color,
            DrawConverting.main_to_draw_coordinates(
                (main_x, camera_y), camera.get_coordinates(), one_tick_to_px),
            DrawConverting.main_to_draw_coordinates(
                (main_x, camera_y - camera_height), camera.get_coordinates(), one_tick_to_px),
            width=1
        )

    @staticmethod
    def draw_horizontal_screen_line(screen: pygame.Surface, camera: Camera, one_tick_to_px: int, main_y: float, color):
        camera_x, _ = camera.get_coordinates()
        camera_width, _ = camera.get_obj_size()
        pygame.draw.line(
            screen, color,
            DrawConverting.main_to_draw_coordinates(
                (camera_x, main_y), camera.get_coordinates(), one_tick_to_px),
            DrawConverting.main_to_draw_coordinates(
                (camera_x + camera_width, main_y), camera.get_coordinates(), one_tick_to_px),
            width=1
        )

    @staticmethod
    def draw_main_axis(screen: pygame.Surface, camera: Camera, one_tick_to_px: int, color):
        Grid.draw_vertical_screen_line(screen, camera, one_tick_to_px, 0, color)
        Grid.draw_horizontal_screen_line(screen, camera, one_tick_to_px, 0, color)

    @staticmethod
    def draw_grid(screen: pygame.Surface, camera: Camera, one_tick_to_px: int, grid_step: int,
                  main_axis_color=AXIS_COLOR, grid_color=GRID_COLOR, text_color=TEXT_COLOR):
        camera_x, camera_y = camera.get_coordinates()
        camera_width, camera_height = camera.get_obj_size()
        start_x = int(camera_x - camera_x % grid_step)
        end_y = int(camera_y - camera_y % grid_step)
        end_x = int(start_x + camera.get_obj_size()[0] + 1)
        start_y = int(end_y - camera.get_obj_size()[1])

        # отображение текста сильно влияет на произвадительность
        # horizontal_text_x = 0
        # if 0 < camera_x:
        #     horizontal_text_x = camera_x
        # elif camera_x + camera_width < 0:
        #     horizontal_text_x = camera_x + camera_width - 20 / one_tick_to_px
        # vertical_text_y = 0
        # if 0 < camera_y - camera_height:
        #     vertical_text_y = camera_y - camera_height + 20 / one_tick_to_px
        # elif camera_y < 0:
        #     vertical_text_y = camera_y

        # Draw vertical grid lines
        count_x = 0
        for x in range(start_x, end_x + 1, grid_step):
            if x == 0:
                Grid.draw_vertical_screen_line(screen, camera, one_tick_to_px, 0, main_axis_color)
                continue
            Grid.draw_vertical_screen_line(screen, camera, one_tick_to_px, x, grid_color)
            # Grid.draw_coordinates(screen, camera, one_tick_to_px, (x, vertical_text_y), text_color, draw_y=False)
            count_x += 1

        # Draw horizontal grid lines
        count_y = 0
        for y in range(start_y, end_y + 1, grid_step):
            if y == 0:
                Grid.draw_horizontal_screen_line(screen, camera, one_tick_to_px, 0, main_axis_color)
                continue
            Grid.draw_horizontal_screen_line(screen, camera, one_tick_to_px, y, grid_color)
            # Grid.draw_coordinates(screen, camera, one_tick_to_px, (horizontal_text_x, y), text_color, draw_x=False)
            count_y += 1

        # Draw axis
        Grid.draw_main_axis(screen, camera, one_tick_to_px, main_axis_color)

        # print(count_x, count_y)
