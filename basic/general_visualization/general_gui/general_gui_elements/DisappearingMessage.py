import pygame

from basic.general_settings import FPS
from basic.general_visualization.general_gui.general_gui_elements.GuiElement import GuiElement
from basic.tools.get_dynamic_alpha import get_dynamic_alpha


class DisappearingMessage(GuiElement):
    def __init__(self, font_size: int = 20, color="white"):
        super().__init__()

        self.message = "Default message"
        self.font_size, self.color = font_size, color
        self.text_font = pygame.font.Font(None, font_size)

        self.time_message_showing = 3  # sec
        self.time_start_decrease_alpha = 2
        self.current_time_message_showing = 0
        self.default_visibility = 255

    def set_font_size(self, font_size: int):
        self.font_size = font_size
        self.text_font = pygame.font.Font(None, font_size)

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

    def draw(self, screen, x: int, y: int):
        if self.current_time_message_showing == 0:
            return
        text = self.text_font.render(f"{self.message}", True, self.color)
        text.set_alpha(get_dynamic_alpha(
            self.time_message_showing, self.time_start_decrease_alpha,
            self.current_time_message_showing, self.default_visibility
        ))
        screen.blit(text, (x, y))

    def update(self):
        self.current_time_message_showing -= 1 / FPS
        if self.current_time_message_showing < 0:
            self.current_time_message_showing = 0

    def show_message(self, screen, x: int, y: int, message: str):
        self.message = message
        self.current_time_message_showing = self.time_message_showing
        self.draw(screen, x, y)
