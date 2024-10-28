from basic.general_game_logic.game_visualization.game_process_visualization.support.ImageLoader import ImageLoader
from basic.tools.get_surface_size_by_screen_proportions import get_surface_size_by_screen_proportions


class GameGraphicScaler(ImageLoader):
    def __init__(self, default_windows_size, default_tick_size):
        super().__init__()
        self.default_windows_size = default_windows_size
        self.default_tick_size = default_tick_size

        self.current_tick_size = default_tick_size

    # set_tick_size actions:

    def get_current_tick_size(self):
        return self.current_tick_size

    def set_tick_size(self, tick_size: int):
        if tick_size < 1:
            raise Exception(f"GameGraphicScaler Error: tick_size = {tick_size} < 1")
        if tick_size != self.current_tick_size:
            self.current_tick_size = tick_size
            self.reload_images(tick_size)

    def auto_set_tick_size(self, screen_size):
        width, height = self.default_windows_size
        new_width, _ = get_surface_size_by_screen_proportions((width, height), screen_size)
        new_tick_size = int(self.default_tick_size * new_width / width)
        self.set_tick_size(new_tick_size)

    def decrease_current_tick_size(self, step: int):
        changed = self.current_tick_size - step
        if changed < 1:
            changed = 1
        self.set_tick_size(changed)

    def increase_current_tick_size(self, step: int):
        changed = self.current_tick_size + step
        print(changed)
        if changed < 1:
            changed = 1
        self.set_tick_size(changed)

    # Load images with tick size

    def load_base_scaling_images(self, images_library):
        self.load_images(images_library, self.get_current_tick_size())

    # Scale actions:

    def scale_size(self, size):
        return (size[0] * self.current_tick_size,
                size[1] * self.current_tick_size)
