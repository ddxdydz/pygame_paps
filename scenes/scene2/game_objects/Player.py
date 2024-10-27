import pygame

from basic.general_settings import FPS
from basic.general_game_logic.base_objects.GameDynamicObject import GameDynamicObject
from basic.general_game_logic.visualization.GameDisplayManager import GamingDisplayManager


class Player(GameDynamicObject):
    DOWN, UP, RIGHT, LEFT = "down", "up", "right", "left"
    frames = {
        DOWN: ["down"],
        UP: ["up"],
        RIGHT: ["right"],
        LEFT: ["left"]
    }
    frames_per_second = {
        DOWN: 1,
        UP: 1,
        RIGHT: 1,
        LEFT: 1
    }
    long_term_stages = ()

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.create_collision_rect(0.35, -0.1, 0.3, 0.8)
        self.audio_manager = None
        self.gaming_gui_manager = None
        self.current_stage = Player.DOWN
        self.enable_updating = True

        self.move_step = 0.02
        self.run_step = 0.06

        # Animated
        self.vertical_reverse = False
        self.current_time = 0
        self.current_frame_index = 0
        self.stage_updating_delay = 0  # frames

    def set_audio_manager(self, audio_manager):
        self.audio_manager = audio_manager

    def load_sound_safety(self, sound_name):
        if self.audio_manager is not None:
            self.audio_manager.load_sound(sound_name)

    def set_gaming_gui_manager(self, gaming_gui_manager):
        self.gaming_gui_manager = gaming_gui_manager

    def show_message_safety(self, message):
        if self.gaming_gui_manager is not None:
            self.gaming_gui_manager.show_message(message)

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = 1 / Player.frames_per_second[self.current_stage]  # sec
            self.current_frame_index += 1
            if self.stage_updating_delay > 0:
                self.stage_updating_delay -= 1
        self.current_frame_index %= len(Player.frames[self.current_stage])

    def process_walking(self):
        keys = pygame.key.get_pressed()
        is_walking = False
        if keys[pygame.K_w]:
            self.move(0, self.move_step)
            is_walking = True
            self.update_stages(Player.UP)
        if keys[pygame.K_s]:
            self.move(0, -self.move_step)
            is_walking = True
            self.update_stages(Player.DOWN)
        if keys[pygame.K_a]:
            self.move(-self.move_step, 0)
            is_walking = True
            self.update_stages(Player.LEFT)
        if keys[pygame.K_d]:
            self.move(self.move_step, 0)
            is_walking = True
            self.update_stages(Player.RIGHT)
        return is_walking

    def process_running(self):
        is_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                self.move(0, self.run_step)
                is_running = True
                self.update_stages(Player.UP)
            if keys[pygame.K_s]:
                self.move(0, -self.run_step)
                is_running = True
                self.update_stages(Player.DOWN)
            if keys[pygame.K_a]:
                self.move(-self.run_step, 0)
                is_running = True
                self.update_stages(Player.LEFT)
            if keys[pygame.K_d]:
                self.move(self.run_step, 0)
                is_running = True
                self.update_stages(Player.RIGHT)
        return is_running

    def process_controller(self):
        is_running = self.process_running()
        if not is_running:
            is_walking = self.process_walking()
            if not is_walking:
                self.update_stages(Player.DOWN)

    def set_stage_updating_delay(self):
        if self.current_stage in Player.long_term_stages:
            self.current_frame_index = 0
            self.stage_updating_delay = len(Player.frames[self.current_stage]) - 1

    def update_stages(self, new_stage=None):
        if not self.stage_updating_delay:
            if new_stage is not None:
                self.current_stage = new_stage
                if self.current_stage in Player.long_term_stages:
                    self.set_stage_updating_delay()

    def update(self):
        if self.enable_updating:
            self.process_controller()
        self.update_stages()
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image(
            "player", Player.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates(),
            self.vertical_reverse
        )
