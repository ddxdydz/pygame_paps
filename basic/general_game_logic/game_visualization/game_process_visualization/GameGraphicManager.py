import pygame

from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.game_visualization.camera_folder.Camera import Camera
from basic.general_game_logic.game_visualization.game_process_visualization.support.GameGraphicScaler import \
    GameGraphicScaler
from basic.general_game_logic.game_visualization.game_process_visualization.support.converting.DrawConverting import \
    DrawConverting
from basic.general_settings import DEFAULT_WINDOW_SIZE, DEFAULT_TICK_SIZE


class GameGraphicManager(GameGraphicScaler):
    def __init__(self, screen, default_windows_size=DEFAULT_WINDOW_SIZE, default_tick_size=DEFAULT_TICK_SIZE):
        super().__init__(default_windows_size, default_tick_size)
        self.screen = screen
        self.camera = Camera()

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def get_camera(self) -> Camera:
        return self.camera

    def to_draw_coordinates(self, x: float, y: float) -> tuple[float, float]:
        return DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), self.get_current_tick_size()
        )

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
                (*self.to_draw_coordinates(x, y), *self.scale_size((width, height))),
                width=int(0.04 * self.get_current_tick_size()) + 1
            )

    def draw_circle(self, x, y, radius, color="gray"):
        if self.check_max_draw_distance(x, y, radius, radius):
            pygame.draw.circle(
                self.screen, color,
                self.to_draw_coordinates(x, y), radius * self.get_current_tick_size(),
                width=int(0.01 * self.get_current_tick_size()) + 1
            )

    def draw_image(self, code, img_type, coordinates, vertical_reverse=False):
        x, y = coordinates
        obj_width, obj_height = self.get_image_size(code)

        if not self.check_max_draw_distance(x, y, obj_width, obj_height):
            return

        draw_coordinates = DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), self.get_current_tick_size())
        img = self.get_image(code, img_type)
        if vertical_reverse:
            img = pygame.transform.flip(img, True, False)
        self.screen.blit(img, draw_coordinates)

    def refresh_screen(self, refresh_color="black"):
        self.screen.fill(refresh_color)

    def update(self):
        self.camera.update(self.screen.get_size(), self.get_current_tick_size())
