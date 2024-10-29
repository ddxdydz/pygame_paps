import pygame


class GuiManagerScene:
    def __init__(self, screen, show_gui=True):
        self.screen = screen
        self.show_gui = show_gui

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def switch_show_gui(self):
        self.show_gui = not self.show_gui

    def set_scale_coefficient(self, scale_coefficient):
        pass

    def update(self):
        pass

    def draw(self):
        pass
