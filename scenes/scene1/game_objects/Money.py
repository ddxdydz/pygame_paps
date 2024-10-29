from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import FPS


class Money(GameCollidingObject):
    frames = ["1", "2", "3", "4"]
    frames_per_second = 5

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.25, -0.25, 0.2, 0.2)
        self.is_collected = False

        # Target
        self.target_object = GameCollidingObject((0, 0))  # default

        # Animated
        self.change_frame_time = 1 / Money.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index = (self.current_frame_index + 1) % len(Money.frames)

    def update(self):
        self.update_frame()

    def draw(self, display_manager: GameVisualizer):
        display_manager.draw_image(
            "money", Money.frames[self.current_frame_index],
            self.get_coordinates()
        )
