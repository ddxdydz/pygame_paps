from basic.general_settings import FPS
from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class Vase(GameCollidingObject):
    CLOSED, OPENING, OPENED = "closed", "opening", "opened"
    frames = {
        CLOSED: ["1"],
        OPENING: ["1", "2", "3", "4"],
        OPENED: ["4"]
    }
    frames_per_second = 4

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.create_collision_rect(0.1, -0.1, 0.5, 0.5)
        self.current_stage = Vase.CLOSED
        self.is_collected = False

        # Animated
        self.change_frame_time = 1 / Vase.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def collect(self):
        if not self.is_collected:
            self.is_collected = True
            self.current_stage = Vase.OPENING
            self.current_time = self.change_frame_time
            self.current_frame_index = 0

    def check_stages(self):
        if self.current_stage == Vase.OPENING:
            if self.current_frame_index == 3:
                self.current_stage = Vase.OPENED
                self.current_frame_index = 0
                self.delete()

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index += 1
        self.current_frame_index %= len(Vase.frames[self.current_stage])

    def update(self):
        self.update_frame()
        self.check_stages()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image(
            "vase", Vase.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates()
        )
