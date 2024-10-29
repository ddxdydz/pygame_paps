import pygame

from basic.basic_gui.gui_elements.general.GuiElement import GuiElement
from basic.general_settings import FPS


class FpsBar(GuiElement):
    def __init__(self):
        super().__init__()

        self.fps = FPS
        self.text_size = 20
        # self.font_size_coefficient = 0.04
        self.red_delta = 0.1  # % / 100

        self.show = False

    def change_show(self):
        self.show = not self.show

    def draw(self, screen, x: int = 0, y: int = 0):
        color = "green" if abs(FPS - self.fps) / FPS < self.red_delta else "red"
        text_size = self.scale_value(self.text_size)
        font = pygame.font.Font(None, text_size)
        text = font.render(f"FPS: {self.fps}", True, color)
        screen.blit(text, (x, y))

    def show_fps(self, screen, fps: int, x: int = 0, y: int = 0):
        if self.show:
            self.fps = fps
            self.draw(screen, x, y)
