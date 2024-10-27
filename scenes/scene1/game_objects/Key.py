from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_game_logic.visualization.GameDisplayManager import GameDisplayManager
from basic.general_settings import FPS


class Key(GameCollidingObject):
    frames = ["1", "2", "3"]
    frames_per_second = 4

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.20, -0.20, 0.3, 0.3)
        self.is_collected = False

        # Target
        self.target_object = GameCollidingObject((0, 0))  # default

        # Animated
        self.change_frame_time = 1 / Key.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def check_target_object_collision(self):
        if not self.is_collected:
            if self.check_collision(self.target_object):
                self.parent_scene.get_audio_manager().load_sound("achievement")
                self.open()

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index = (self.current_frame_index + 1) % len(Key.frames)

    def update(self):
        self.update_frame()

    def draw(self, display_manager: GameDisplayManager):
        display_manager.draw_image(
            "key", Key.frames[self.current_frame_index],
            self.get_coordinates()
        )
