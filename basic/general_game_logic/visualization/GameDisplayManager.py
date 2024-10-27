import pygame

from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.camera_folder.Camera import Camera
from basic.general_game_logic.visualization.converting.DrawConverting import DrawConverting
from basic.general_settings import ONE_TICK_TO_PX
from basic.general_visualization.ImageLoader import ImageLoader


class GameDisplayManager(ImageLoader):
    def __init__(self, screen):
        super().__init__(ONE_TICK_TO_PX)
        self.screen = screen
        self.camera = Camera()

    def get_screen(self):
        return self.screen

    def get_camera(self):
        return self.camera

    def set_size_tick_scale(self, size_tick_scale):
        if size_tick_scale < 0:
            size_tick_scale = 0
        self.size_tick_scale = size_tick_scale
        self.camera.update_visualization_parameters(
            self.screen.get_size(), size_tick_scale
        )

    def auto_set_size_tick_scale(self):
        pass

    def to_draw_coordinates(self, x, y):
        return DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), self.size_tick_scale
        )

    def check_max_draw_distance(self, obj_x, obj_y, obj_width, obj_height) -> bool:
        checking_obj = GameObject((obj_x, obj_y), (obj_width, obj_height))
        max_draw_distance = self.camera.get_no_contact_distance(checking_obj)
        if self.camera.get_distance_between_centres(checking_obj) < max_draw_distance:
            return True
        return False

    def draw_rect(self, x, y, width, height, color="blue"):
        if self.check_max_draw_distance(x, y, width, height):
            scaled_size = width * self.size_tick_scale, height * self.size_tick_scale
            pygame.draw.rect(
                self.screen, color,
                (*self.to_draw_coordinates(x, y), *scaled_size),
                width=int(0.04 * self.size_tick_scale) + 1
            )

    def draw_circle(self, x, y, radius, color="gray"):
        if self.check_max_draw_distance(x, y, radius, radius):
            pygame.draw.circle(
                self.screen, color,
                self.to_draw_coordinates(x, y), radius * self.size_tick_scale,
                width=int(0.01 * self.size_tick_scale) + 1
            )

    def draw_image(self, code, img_type, coordinates, vertical_reverse=False):
        x, y = coordinates
        obj_width, obj_height = self.get_image_size(code)

        if not self.check_max_draw_distance(x, y, obj_width, obj_height):
            return

        draw_coordinates = DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), self.size_tick_scale)
        img = self.get_image(code, img_type)
        if vertical_reverse:
            img = pygame.transform.flip(img, True, False)
        self.screen.blit(img, draw_coordinates)

    def refresh_screen(self, refresh_color="black"):
        self.screen.fill(refresh_color)

    def update(self):
        self.camera.update()
        self.camera.update_visualization_parameters(
            self.screen.get_size(), self.size_tick_scale
        )
