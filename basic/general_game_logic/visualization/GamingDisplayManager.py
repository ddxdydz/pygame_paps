import pygame

from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.visualization.converting.DrawConverting import DrawConverting
from basic.general_game_logic.game_base_settings import ONE_TICK_TO_PX
from basic.tools.loading_files import load_image


class GamingDisplayManager:
    def __init__(self, camera, screen):
        self.loaded_images = dict()
        self.camera = camera
        self.screen = screen

    def load_images(self, images_library):
        for code in images_library.keys():
            width, height = images_library[code]["size"]
            self.loaded_images[code] = dict()
            for img_type, path in images_library[code]["imgs"].items():
                img = load_image(path, size=(width * ONE_TICK_TO_PX, height * ONE_TICK_TO_PX))
                self.loaded_images[code][img_type] = img  # fillness
                self.loaded_images[code]["size"] = width, height

    def update_screen(self, screen):
        self.screen = screen

    def to_draw_coordinates(self, x, y):
        return DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), ONE_TICK_TO_PX
        )

    def get_img(self, obj_code, img_type):
        return self.loaded_images[obj_code][img_type]

    def check_max_draw_distance(self, obj_x, obj_y, obj_width, obj_height) -> bool:
        checking_obj = GameObject((obj_x, obj_y), (obj_width, obj_height))
        max_draw_distance = self.camera.get_no_contact_distance(checking_obj)
        if self.camera.get_distance_between_centres(checking_obj) < max_draw_distance:
            return True
        return False

    def draw_rect(self, x, y, width, height, color="blue"):
        if self.check_max_draw_distance(x, y, width, height):
            pygame.draw.rect(
                self.screen, color,
                (*self.to_draw_coordinates(x, y), width * ONE_TICK_TO_PX, height * ONE_TICK_TO_PX),
                width=int(0.04 * ONE_TICK_TO_PX) + 1
            )

    def draw_circle(self, x, y, radius, color="gray"):
        if self.check_max_draw_distance(x, y, radius, radius):
            pygame.draw.circle(
                self.screen, color,
                self.to_draw_coordinates(x, y), radius * ONE_TICK_TO_PX,
                width=int(0.01 * ONE_TICK_TO_PX) + 1
            )

    def draw_image(self, obj_code, img_type, coordinates, vertical_reverse=False):
        x, y = coordinates
        obj_width, obj_height = self.loaded_images[obj_code]["size"]
        if self.check_max_draw_distance(x, y, obj_width, obj_height):
            draw_coordinates = DrawConverting.main_to_draw_coordinates(
                (x, y), self.camera.get_coordinates(), ONE_TICK_TO_PX)
            img = self.get_img(obj_code, img_type)
            if vertical_reverse:
                img = pygame.transform.flip(img, True, False)
            self.screen.blit(img, draw_coordinates)
