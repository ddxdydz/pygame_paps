import pygame

from basic.tools.screen_placement.get_drawing_center_coordinates import get_drawing_center_coordinates


class ExternalMargins:
    """
    margin value = (percent_of_parent_screen_size / 100)
    margin value < 0 => right margin placement
    margin value > 0 => left margin placement
    margin value = 0 => center placement
    """
    def __init__(self, margin_x=0, margin_y=0):
        self.margin_x = margin_x
        self.margin_y = margin_y

    @staticmethod
    def get_drawing_x_by_left_padding(margin_x, parent_surface_width: int) -> int:
        padding_px = parent_surface_width * abs(margin_x) / 100
        return int(padding_px)

    @staticmethod
    def get_drawing_x_by_right_padding(margin_x, parent_surface_width: int, child_surface_width: int) -> int:
        padding_px = parent_surface_width * abs(margin_x) / 100
        return int(parent_surface_width - child_surface_width - padding_px)

    @staticmethod
    def get_drawing_y_by_upper_padding(margin_y, parent_surface_height: int) -> int:
        padding_px = parent_surface_height * abs(margin_y) / 100
        return int(padding_px)

    @staticmethod
    def get_drawing_y_by_down_padding(margin_y, parent_surface_height: int, child_surface_height: int) -> int:
        padding_px = parent_surface_height * abs(margin_y) / 100
        return int(parent_surface_height - child_surface_height - padding_px)

    def get_drawing_coordinates(self, parent_surface: pygame.Surface, child_surface: pygame.Surface) -> tuple[int, int]:
        x, y = get_drawing_center_coordinates(parent_surface, child_surface)
        if self.margin_x > 0:
            x = self.get_drawing_x_by_left_padding(
                self.margin_x, parent_surface.get_width())
        elif self.margin_x < 0:
            x = self.get_drawing_x_by_right_padding(
                self.margin_x, parent_surface.get_width(), child_surface.get_width())
        if self.margin_y > 0:
            y = self.get_drawing_y_by_upper_padding(
                self.margin_y, parent_surface.get_height())
        elif self.margin_y < 0:
            y = self.get_drawing_y_by_down_padding(
                self.margin_y, parent_surface.get_height(), child_surface.get_height())
        return x, y

    def get_drawing_coordinates_by_sizes(
            self, parent_surface_size: tuple[int, int],
            child_surface_size: tuple[int, int]) -> tuple[int, int]:
        return self.get_drawing_coordinates(
            pygame.Surface(parent_surface_size),
            pygame.Surface(child_surface_size)
        )

