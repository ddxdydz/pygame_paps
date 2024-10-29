import pygame

from basic.basic_gui.gui_elements.StatusBar import StatusBar
from basic.tools.loading.loading_files import load_image


class StaminaBar:
    def __init__(self, image_path=None):
        self.bar = StatusBar(200, 20, color=(255, 170, 11))

        self.left_filling_indent = 22
        self.upper_filling_indent = 16

        self.right_padding = 3  # px
        self.upper_padding = 60

        self.surface_size = (225, 50)
        self.image = pygame.Surface(self.surface_size)
        self.image.fill("pink")
        self.image.set_colorkey("pink")
        if image_path is not None:
            self.set_image(image_path)

    def set_image(self, path):
        self.image = load_image(path, self.surface_size)

    def update_stamina_bar(self, current_value, max_value):
        self.bar.update_filling_level(current_value / max_value)

    def draw_stamina_bar(self, screen):
        bar_panel = pygame.Surface(self.image.get_size())
        bar_panel.fill("pink")
        bar_panel.set_colorkey("pink")
        self.bar.draw(bar_panel, self.left_filling_indent, self.upper_filling_indent)
        bar_panel.blit(self.image)
        screen.blit(bar_panel, (screen.get_width() - bar_panel.get_width() - self.right_padding, self.upper_padding))
