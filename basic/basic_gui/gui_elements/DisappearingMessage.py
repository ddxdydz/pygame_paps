import pygame

from basic.basic_gui.gui_elements.general.GuiElement import GuiElement
from basic.general_settings import FPS
from basic.tools.get_dynamic_alpha import get_dynamic_alpha


class DisappearingMessage(GuiElement):
    def __init__(self):
        super().__init__()

        self.message = "Default message"
        self.font_size, self.color = 30, "white"

        self.time_message_showing = 3  # sec
        self.time_start_decrease_alpha = 2
        self.current_time_message_showing = 0
        self.default_visibility = 255

    def set_font_size(self, font_size: int):
        self.font_size = font_size

    def set_color(self, color):
        self.color = color

    def set_default_visibility(self, default_visibility):
        if default_visibility < 0 or default_visibility > 255:
            raise Exception("DisappearingMessage: default_visibility < 0 or default_visibility > 255")
        self.default_visibility = default_visibility

    def set_time_message_showing(self, time: float):
        self.time_message_showing = time

    def set_time_start_decrease_alpha(self, time: float):
        self.time_start_decrease_alpha = time

    def update(self):
        self.current_time_message_showing -= 1 / FPS
        if self.current_time_message_showing < 0:
            self.current_time_message_showing = 0

    def show_message(self, message: str):
        self.message = message
        self.current_time_message_showing = self.time_message_showing

    def draw(self, screen, x: int, y: int):
        if self.current_time_message_showing == 0:
            return
        font = pygame.font.Font(None, self.font_size)
        text = font.render(f"{self.message}", True, self.color)
        text.set_alpha(get_dynamic_alpha(
            self.time_message_showing, self.time_start_decrease_alpha,
            self.current_time_message_showing, self.default_visibility
        ))
        screen.blit(text, (x, y))
