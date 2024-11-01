import pygame

from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.game_visualization.camera_folder.Camera import Camera
from basic.general_game_logic.game_visualization.support_visualization_components.GameGraphicScaler import \
    GameGraphicScaler
from basic.general_game_logic.game_visualization.support_visualization_components.converting.DrawConverting import \
    DrawConverting
from basic.general_settings import DEFAULT_WINDOW_SIZE, DEFAULT_TICK_SIZE


class GameVisualizer(GameGraphicScaler):
    def __init__(self, screen, default_windows_size=DEFAULT_WINDOW_SIZE, default_tick_size=DEFAULT_TICK_SIZE):
        super().__init__(default_windows_size, default_tick_size)
        self.screen = screen
        self.camera = Camera()

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def get_camera(self) -> Camera:
        return self.camera

    def to_main_coordinates(self, x: int, y: int) -> tuple[float, float]:
        return DrawConverting.draw_to_main_coordinates(
            (x, y), self.camera.get_coordinates(), self.get_current_tick_size()
        )

    def to_draw_coordinates(self, x: float, y: float) -> tuple[int, int]:
        return DrawConverting.main_to_draw_coordinates(
            (x, y), self.camera.get_coordinates(), self.get_current_tick_size()
        )

    def check_max_draw_distance(self, obj_x, obj_y, obj_width, obj_height) -> bool:
        checking_obj = GameObject((obj_x, obj_y), (obj_width, obj_height))
        max_draw_distance = self.camera.get_no_contact_distance(checking_obj)  # // 2
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

        img = self.get_image(code, img_type)
        if vertical_reverse:
            img = pygame.transform.flip(img, True, False)

        self.screen.blit(img, self.to_draw_coordinates(x, y))

    def draw_image_by_cameras_area(self, code, img_type, coordinates):
        x, y = coordinates
        # img_width, img_height = tuple(int(self.get_current_tick_size() * value)
        # for value in self.get_image_size(code))

        area = self.camera.get_x() - x, -(self.camera.get_y() - y), *self.camera.get_size()
        area = tuple(int(self.get_current_tick_size() * value) for value in area)
        # area_x0, area_y0, area_width, area_height = area
        # area_x1, area_y1 = area_x0 + area_width, area_y0 + area_height
        #
        # if area_x0 < 0: area_x0 = 0
        # if area_y0 < 0: area_y0 = 0
        # if area_x1 > img_width: area_x1 = img_width
        # if area_y1 > img_height: area_y1 = img_height
        #
        # count = 0
        # for cx in range(area_x0, area_x1 + 1):
        #     for cy in range(area_y0, area_y1 + 1):
        #         count += 1
        # print(count, (area_x0, area_x1), (area_y0, area_y1), area)

        self.screen.blit(
            self.get_image(code, img_type),
            (0, 0),
            area=area
        )

    def refresh_screen(self, refresh_color="black"):
        self.screen.fill(refresh_color)

    def update(self):
        self.camera.update(self.screen.get_size(), self.get_current_tick_size())
