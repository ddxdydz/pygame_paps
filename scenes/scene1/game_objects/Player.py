import pygame

from basic.general_game_logic.base_objects.GameAnimatedObject import GameAnimatedObject
from basic.general_game_logic.base_objects.GameCombatObject import GameCombatObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.dynamic.combat_system.Stamina import Stamina
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import FPS
from scenes.scene1.general.scene_settings import PLAYER_ANIMATION


class Player(GameCombatObject, GameAnimatedObject):
    ATTACK, STAY, DEAD, DEATH, WALK, RUN, HIT = PLAYER_ANIMATION.keys()

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        GameAnimatedObject.__init__(self, Player.STAY, PLAYER_ANIMATION)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.35, -0.3, 0.3, 0.6)
        self.enable_updating = True
        self.vertical_reverse = False

        # Moving speed
        self.move_step = 1.2 / FPS
        self.run_step = 3 / FPS

        # Stamina
        self.stamina_keeper = Stamina()
        self.stamina_keeper.set_parameters(100, 100)

        # Combat Parameters
        self.set_damage_parameters(CollisionRect(0.1, -0.3, 0.8, 0.6), 20)
        self.set_health_parameters(100, 100)

    def take_hit(self, damage):
        if self.health_keeper.health == 0:
            return
        self.health_keeper.take_damage(damage)
        self.parent_scene.get_scene_gui_manager().show_message(
            f"- Вы получили урон: {damage}. Текущее количество hp: {self.health_keeper.health}"
        )
        self.parent_scene.get_audio_manager().load_sound("hero_hit")
        self.change_stage(Player.HIT)

    def check_death(self):
        if not self.health_keeper.is_died():
            return
        self.parent_scene.get_audio_manager().load_sound("death")
        self.change_stage(Player.DEAD)
        self.enable_updating = False

    def process_running(self) -> bool:
        is_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and self.stamina_keeper.current_stamina > 0:
            if keys[pygame.K_w]:
                self.move(0, self.run_step)
                is_running = True
            if keys[pygame.K_s]:
                self.move(0, -self.run_step)
                is_running = True
            if keys[pygame.K_a]:
                self.move(-self.run_step, 0)
                is_running = True
                self.vertical_reverse = True
            if keys[pygame.K_d]:
                self.move(self.run_step, 0)
                is_running = True
                self.vertical_reverse = False
        return is_running

    def process_walking(self) -> bool:
        keys = pygame.key.get_pressed()
        is_walking = False
        if keys[pygame.K_w]:
            self.move(0, self.move_step)
            is_walking = True
        if keys[pygame.K_s]:
            self.move(0, -self.move_step)
            is_walking = True
        if keys[pygame.K_a]:
            self.move(-self.move_step, 0)
            is_walking = True
            self.vertical_reverse = True
        if keys[pygame.K_d]:
            self.move(self.move_step, 0)
            is_walking = True
            self.vertical_reverse = False
        return is_walking

    def process_attacking(self) -> bool:
        keys = pygame.key.get_pressed()
        is_attacking = False
        if keys[pygame.K_e]:
            if self.current_stage != Player.ATTACK:
                is_attacking = True
        return is_attacking

    def process_controller(self):
        if self.current_stage == Player.HIT:
            return
        if not self.enable_updating:
            return

        is_walking = self.process_walking()
        is_running = self.process_running()
        is_attacking = self.process_attacking()

        if is_running:
            self.change_stage(Player.RUN)
            self.stamina_keeper.decrease()
        elif is_walking:
            self.change_stage(Player.WALK)
        else:
            self.change_stage(Player.STAY)

        if is_attacking:
            self.change_stage(Player.ATTACK)

    def process_last_frame(self):
        if self.check_stage_end(Player.ATTACK):
            self.attack()
        if self.check_stage_end(Player.HIT):
            self.check_death()

    def update(self):
        if self.enable_updating:
            self.stamina_keeper.update()
        self.update_frame()
        self.process_last_frame()

    def draw(self, game_visualizer: GameVisualizer):
        game_visualizer.draw_image(
            "hero", self.get_frame_code(),
            self.get_coordinates(),
            self.vertical_reverse
        )
