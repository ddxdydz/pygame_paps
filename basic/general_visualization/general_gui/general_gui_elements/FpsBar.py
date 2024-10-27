import pygame

from basic.general_settings import FPS
from basic.general_visualization.general_gui.general_gui_elements.GuiElement import GuiElement


class FpsBar(GuiElement):
    def __init__(self):
        super().__init__()

        self.fps = FPS
        self.font_size_coefficient = 0.04
        self.text_font = pygame.font.Font(None, 20)
        self.red_delta = 0.1  # % / 100

        self.show = False

    def change_show(self):
        self.show = not self.show

    def set_font_size(self, font_size: int):
        self.text_font = pygame.font.Font(None, font_size)

    def draw(self, screen, x: int = 0, y: int = 0):
        color = "green" if abs(FPS - self.fps) / FPS < self.red_delta else "red"
        self.set_font_size(int(screen.get_height() * self.font_size_coefficient))
        text = self.text_font.render(f"FPS: {self.fps}", True, color)
        screen.blit(text, (x, y))

    def show_fps(self, screen, fps: int, x: int = 0, y: int = 0):
        if self.show:
            self.fps = fps
            self.draw(screen, x, y)
