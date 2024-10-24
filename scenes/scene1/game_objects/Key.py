from basic.general_settings import FPS
from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class Key(GameCollidingObject):
    frames = ["1", "2", "3"]
    frames_per_second = 4

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.create_collision_rect(0.20, -0.20, 0.3, 0.3)
        self.is_collected = False

        # Animated
        self.change_frame_time = 1 / Key.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index = (self.current_frame_index + 1) % len(Key.frames)

    def update(self):
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image(
            "key", Key.frames[self.current_frame_index],
            self.get_coordinates()
        )
