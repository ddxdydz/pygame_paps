from math import ceil

import pygame

from basic.general_settings import DEFAULT_GGUI_SCALE_COEFFICIENT
from basic.tools.create_error_surface import create_error_surface


class GuiElement:
    def __init__(self, show=True, scale_coefficient=DEFAULT_GGUI_SCALE_COEFFICIENT):
        self.show = show
        self.scale_coefficient = 1
        self.set_scale_coefficient(scale_coefficient)

    def set_scale_coefficient(self, scale_coefficient: float):
        if scale_coefficient <= 0:
            raise Exception(f"GuiElement Error: scale_coefficient = {scale_coefficient} <= 0")
        self.scale_coefficient = scale_coefficient

    def get_scale_coefficient(self) -> float:
        return self.scale_coefficient

    def scale_value(self, value) -> int:
        return ceil(self.scale_coefficient * value)

    def scale_size(self, width: int, height: int) -> tuple[int, int]:
        return self.scale_value(width), self.scale_value(height)

    def switch_show(self):
        self.show = not self.show

    def is_show(self) -> bool:
        return self.show

    def draw(self, screen: pygame.Surface, x: int, y: int):
        if self.show:
            error_surface = create_error_surface(20, 20, color="red")
            screen.blit(error_surface, (x, y))

    def update(self):
        pass
