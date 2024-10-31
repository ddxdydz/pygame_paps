import pygame

from basic.basic_gui.gui_elements.DisappearingMessage import DisappearingMessage


class GuiManagerScene:
    def __init__(self, screen, show_gui=True):
        self.screen = screen
        self.show_gui = show_gui
        self.messanger = DisappearingMessage()

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def switch_show_gui(self):
        self.show_gui = not self.show_gui

    def show_message(self, message: str):
        self.messanger.show_message(message)

    def set_scale_coefficient(self, scale_coefficient):
        pass

    def update(self):
        self.messanger.update()

    def draw(self):
        if self.show_gui:
            self.messanger.draw(self.get_screen(), 20, 30)
