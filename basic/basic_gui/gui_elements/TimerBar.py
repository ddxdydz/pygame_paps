import pygame

from basic.basic_gui.gui_elements.general.GuiElement import GuiElement
from basic.general_settings import FPS
from basic.tools.screen_placement.ExternalMargins import ExternalMargins


class TimerBar(GuiElement):
    def __init__(self):
        super().__init__()
        self.font_size, self.color = 40, "white"
        self.default_visibility = 200

        self.placement = ExternalMargins(0, 0.1)

        self.process_time = False
        self.current_timer_value = 0
        self.switch_show()

    def set_font_size(self, font_size: int):
        self.font_size = font_size

    def set_color(self, color):
        self.color = color

    def start(self):
        self.process_time = True

    def stop(self):
        self.process_time = False

    def get_time(self):
        return round(self.current_timer_value, 1)

    def update(self):
        if self.process_time:
            self.current_timer_value += 1 / FPS

    def draw(self, screen, x: int = None, y: int = None):
        if self.show:
            font = pygame.font.Font(None, self.font_size)
            text = font.render(f"{self.get_time()} sec", True, self.color)
            text.set_alpha(self.default_visibility)
            screen.blit(text, self.placement.get_drawing_coordinates(screen, text))
