from basic.general_game_logic.base_objects.GameCollidingObject import GameCollidingObject
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_game_logic.game_visualization.game_process_visualization.GameGraphicManager import GameGraphicManager
from basic.general_settings import FPS


class Chess(GameCollidingObject):
    CLOSED, OPENING, OPENED = "closed", "opening", "opened"
    frames = {
        CLOSED: ["1"],
        OPENING: ["1", "2", "3", "4"],
        OPENED: ["4"]
    }
    frames_per_second = 4

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.1, -0.1, 0.5, 0.5)
        self.current_stage = Chess.CLOSED
        self.is_collected = False

        # Target
        self.target_object = GameCollidingObject((0, 0))  # default

        # Animated
        self.change_frame_time = 1 / Chess.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def open(self):
        if not self.is_collected:
            self.is_collected = True
            self.current_stage = Chess.OPENING
            self.current_time = self.change_frame_time
            self.current_frame_index = 0

    def check_target_object_collision(self):
        if self.parent_scene.current_player_statistic["key_count"] == 1 and self.current_stage == Chess.CLOSED:
            if self.check_collision(self.target_object):
                self.parent_scene.get_audio_manager().load_sound("achievement")
                self.open()

    def check_stages(self):
        if self.current_stage == Chess.OPENING:
            if self.current_frame_index == 3:
                self.current_stage = Chess.OPENED
                self.current_frame_index = 0

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index += 1
        self.current_frame_index %= len(Chess.frames[self.current_stage])

    def update(self):
        self.update_frame()
        self.check_stages()
        self.check_target_object_collision()

    def draw(self, display_manager: GameGraphicManager):
        display_manager.draw_image(
            "chess", Chess.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates()
        )
