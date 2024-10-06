from math import hypot

import pygame

from basic.game_logic.visualization.converting.DrawConverting import DrawConverting
from basic.local_constants import WINDOW_SIZE
from basic.loading_files import load_image
from basic.game_logic.game_constants import CODES_TABLE, OBJECTS_SETTINGS, ONE_TICK_TO_PX


class GamingDisplayManager:
    objects_images_library = dict()
    for code, name in CODES_TABLE.items():
        width, height = OBJECTS_SETTINGS[name]["size"]
        objects_images_library[code] = dict()
        for img_type, path in OBJECTS_SETTINGS[name]["imgs"].items():
            img = load_image(path, size=(width * ONE_TICK_TO_PX, height * ONE_TICK_TO_PX))
            objects_images_library[code][img_type] = img

    def __init__(self, camera, screen):
        self.camera = camera
        self.screen = screen

    def update_screen(self, screen):
        self.screen = screen

    @staticmethod
    def get_img(obj_code, img_type):
        return GamingDisplayManager.objects_images_library[obj_code][img_type]

    def get_camera_size_in_ticks(self):
        camera_size_in_px = camera_width_in_px, camera_height_in_px = WINDOW_SIZE
        return camera_width_in_px // ONE_TICK_TO_PX, camera_height_in_px // ONE_TICK_TO_PX

    def check_max_draw_distance(self, obj_code, x, y) -> bool:
        obj_width, obj_height = OBJECTS_SETTINGS[CODES_TABLE[obj_code]]["size"]
        obj_center_x, obj_center_y = x + obj_width / 2, y - obj_height / 2

        camera_width, camera_height = self.get_camera_size_in_ticks()
        camera_x, camera_y = self.camera.get_coordinates()
        camera_center_x, camera_center_y = camera_x + camera_width / 2, camera_y - camera_height / 2

        max_draw_distance = (hypot(obj_width, obj_height) + hypot(camera_width, camera_height)) * 0.6
        distance = hypot(abs(obj_center_x - camera_center_x), abs(obj_center_y - camera_center_y))
        if distance < max_draw_distance:
            return True
        return False

    def draw_collision(self, obj_code, obj_rect_points, coordinates):
        x, y = coordinates
        if self.check_max_draw_distance(obj_code, x, y):
            updated_points = []
            for rx, ry in obj_rect_points:
                draw_coordinates = DrawConverting.main_to_draw_coordinates(
                    (rx + x, ry + y), self.camera.get_coordinates(), ONE_TICK_TO_PX)
                updated_points.append(draw_coordinates)
            pygame.draw.polygon(
                self.screen, "blue",
                updated_points,
                width=int(0.02 * ONE_TICK_TO_PX) + 1
            )

    def draw(self, obj_code, img_type, coordinates, vertical_reverse=False):
        x, y = coordinates
        if self.check_max_draw_distance(obj_code, x, y):
            draw_coordinates = DrawConverting.main_to_draw_coordinates(
                (x, y), self.camera.get_coordinates(), ONE_TICK_TO_PX)
            img = GamingDisplayManager.objects_images_library[obj_code][img_type]
            if vertical_reverse:
                img = pygame.transform.flip(img, True, False)
            self.screen.blit(img, draw_coordinates)
