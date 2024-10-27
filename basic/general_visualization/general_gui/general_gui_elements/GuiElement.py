from basic.tools.create_error_surface import create_error_surface


class GuiElement:
    def __init__(self):
        pass

    def draw(self, screen, x: int, y: int):
        screen.blit(create_error_surface(20, 20, color="red"), (x, y))

    def update(self):
        pass
