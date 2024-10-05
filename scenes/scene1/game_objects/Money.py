from basic.local_constants import FPS
from basic.game_logic.GameCollidingObject import GameCollidingObject
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class Money(GameCollidingObject):
    CODE = "mn"
    frames = ["1", "2", "3", "4"]
    frames_per_second = 5

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.set_collision_rect(0.25, -0.25, 0.2, 0.2)
        self.is_collected = False

        # Animated
        self.change_frame_time = 1 / Money.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def get_code(self):
        return Money.CODE

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index = (self.current_frame_index + 1) % len(Money.frames)

    def update(self):
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw(
            Money.CODE, Money.frames[self.current_frame_index],
            self.get_coordinates()
        )
