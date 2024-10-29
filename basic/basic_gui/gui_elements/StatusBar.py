import pygame

from basic.basic_gui.gui_elements.general.GuiElement import GuiElement


class StatusBar(GuiElement):
    def __init__(self, width: int, height: int, is_horizontal: bool = True, color="blue"):
        super().__init__()
        self.width, self.height = width, height
        self.is_horizontal = is_horizontal
        if color == "pink":
            raise Exception("No pink in status bar")  # pink is colorkey
        self.color = color
        self.filling_level = 0.2

    def set_size(self, width, height):
        self.width, self.height = width, height

    def update_filling_level(self, level: float):
        if level < 0 or level > 1:
            raise Exception("StatusBar Error: level < 0 or level > 1")
        self.filling_level = level
    
    def create_bar(self) -> pygame.Surface:
        bar_surface = pygame.Surface((self.width, self.height))
        bar_surface.fill("pink")
        bar_surface.set_colorkey("pink")

        filling_width, filling_height = self.width, self.height
        if self.is_horizontal:
            filling_width *= self.filling_level
        else:
            filling_height *= self.filling_level

        pygame.draw.rect(
            bar_surface, self.color, ((0, 0), self.scale_size(filling_width, filling_height))
        )

        return bar_surface

    def draw(self, screen, x, y):
        screen.blit(self.create_bar(), (x, y))
