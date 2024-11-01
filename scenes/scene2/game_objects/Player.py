import pygame

from basic.general_game_logic.base_objects.GameAnimatedObject import GameAnimatedObject
from basic.general_game_logic.base_objects.GameCombatObject import GameCombatObject
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import FPS
from scenes.scene2.general.scene_settings import PLAYER_ANIMATION


class Player(GameCombatObject, GameAnimatedObject):
    DOWN, UP, LEFT, RIGHT = PLAYER_ANIMATION.keys()

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        GameAnimatedObject.__init__(self, Player.DOWN, PLAYER_ANIMATION)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.35, -0.3, 0.3, 0.6)
        self.enable_updating = True
        self.move_direction = self.DOWN

        # Moving speed
        self.move_step = 1.2 / FPS
        self.run_step = 3 / FPS

    def process_running(self) -> bool:
        is_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                self.move(0, self.run_step)
                is_running = True
                self.move_direction = Player.UP
            if keys[pygame.K_s]:
                self.move(0, -self.run_step)
                is_running = True
                self.move_direction = Player.DOWN
            if keys[pygame.K_a]:
                self.move(-self.run_step, 0)
                is_running = True
                self.move_direction = Player.LEFT
            if keys[pygame.K_d]:
                self.move(self.run_step, 0)
                is_running = True
                self.move_direction = Player.RIGHT
        return is_running

    def process_walking(self) -> bool:
        keys = pygame.key.get_pressed()
        is_walking = False
        if keys[pygame.K_w]:
            self.move(0, self.move_step)
            is_walking = True
            self.move_direction = Player.UP
        if keys[pygame.K_s]:
            self.move(0, -self.move_step)
            is_walking = True
            self.move_direction = Player.DOWN
        if keys[pygame.K_a]:
            self.move(-self.move_step, 0)
            is_walking = True
            self.move_direction = Player.LEFT
        if keys[pygame.K_d]:
            self.move(self.move_step, 0)
            is_walking = True
            self.move_direction = Player.RIGHT
        return is_walking

    def process_controller(self):
        if not self.enable_updating:
            return

        is_walking = self.process_walking()
        is_running = self.process_running()

        if is_running:
            self.change_stage(self.move_direction)
        elif is_walking:
            self.change_stage(self.move_direction)
        else:
            self.change_stage(Player.DOWN)

    def process_last_frame(self):
        pass

    def update(self):
        self.update_frame()
        self.process_last_frame()

    def draw(self, game_visualizer: GameVisualizer):
        game_visualizer.draw_image(
            "player", self.get_frame_code(),
            self.get_coordinates()
        )
