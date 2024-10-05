import pygame

from basic.local_constants import FPS
from basic.game_logic.GameDynamicObject import GameDynamicObject
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class Player(GameDynamicObject):
    CODE = "hr"
    ATTACK, STAY, DEAD, DEATH, WALK, RUN = "attack", "stay", "dead", "death", "walk", "run"
    frames = {
        ATTACK: ["attack1", "attack2", "attack3", "attack4", "attack5"],
        STAY: ["attack1"],
        DEAD: ["dead1", "dead2", "dead3", "dead4", "dead5", "dead6"],
        DEATH: ["dead6"],
        WALK: ["walk1", "walk2", "walk3", "walk4", "walk5"],
        RUN: ["run1", "run2", "run3", "run4", "run5", "run6", "run7"]
    }
    frames_per_second = 5

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.set_collision_rect(0.35, -0.3, 0.3, 0.6)
        self.current_stage = Player.STAY
        self.move_step = 0.02
        self.run_step = 0.05
        self.enable_updating = True

        # Animated
        self.vertical_reverse = False
        self.change_frame_time = 1 / Player.frames_per_second  # sec
        self.current_time = 0
        self.current_frame_index = 0

    def get_code(self):
        return Player.CODE

    def update_frame(self):
        self.current_time -= 1 / FPS
        if self.current_time < 0:
            self.current_time = self.change_frame_time
            self.current_frame_index += 1
        self.current_frame_index %= len(Player.frames[self.current_stage])

    def keys_update(self):
        keys = pygame.key.get_pressed()
        is_walking = False
        is_running = False

        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                self.add_processing_move(0, self.run_step)
                is_running = True
            if keys[pygame.K_s]:
                self.add_processing_move(0, -self.run_step)
                is_running = True
            if keys[pygame.K_a]:
                self.add_processing_move(-self.run_step, 0)
                is_running = True
                self.vertical_reverse = True
            if keys[pygame.K_d]:
                self.add_processing_move(self.run_step, 0)
                is_running = True
                self.vertical_reverse = False
        else:
            if keys[pygame.K_w]:
                self.add_processing_move(0, self.move_step)
                is_walking = True
            if keys[pygame.K_s]:
                self.add_processing_move(0, -self.move_step)
                is_walking = True
            if keys[pygame.K_a]:
                self.add_processing_move(-self.move_step, 0)
                is_walking = True
                self.vertical_reverse = True
            if keys[pygame.K_d]:
                self.add_processing_move(self.move_step, 0)
                is_walking = True
                self.vertical_reverse = False

        if is_walking:
            self.current_stage = Player.WALK
        elif is_running:
            self.current_stage = Player.RUN
        else:
            if keys[pygame.K_e]:
                self.current_stage = Player.ATTACK
            else:
                self.current_stage = Player.STAY

    def update(self):
        if self.enable_updating:
            self.keys_update()
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw(
            Player.CODE, Player.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates(),
            self.vertical_reverse
        )
