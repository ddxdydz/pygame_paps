from math import inf

from basic.general_game_logic.base_objects.GameAnimatedObject import GameAnimatedObject
from basic.general_game_logic.base_objects.GameCombatObject import GameCombatObject
from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import FPS
from scenes.scene3.general.scene_settings import SHADOW_ANIMATION
from scenes.scene1.map.layers_generator.get_scheme_coordinates import get_scheme_coordinates
from scenes.scene1.map.layers_generator.maze.maze_solver import bfs


class Shadow(GameCombatObject, GameAnimatedObject):
    ATTACK, STAY, DEAD, DEATH, WALK, HIT, REACT = SHADOW_ANIMATION.keys()

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        GameAnimatedObject.__init__(self, self.STAY, SHADOW_ANIMATION)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.25, -0.1, 0.5, 0.8)
        self.vertical_reverse = False
        self.enable_updating = True

        # Moving speed
        self.move_step = 1.2 / FPS
        self.run_step = 3 / FPS

        # Combat Parameters
        self.set_damage_parameters(CollisionRect(0.15, 0, 0.7, 1), 34)
        self.set_health_parameters(100, 100)
        self.infinity_health = False

        # Enemy parameters
        self.target_object = None
        self.map_collision_scheme = None
        self.start_attack_distance = 0.8
        self.alert_distance = 3  # ticks
        self.is_alert = False

    def set_target_object(self, obj: GameObject):
        self.target_object = obj

    def take_hit(self, damage):
        if self.health_keeper.health == 0:
            return
        self.health_keeper.take_damage(damage)
        self.parent_scene.get_scene_gui_manager().show_message(
            f"- Shadow получил дамаг: {damage}. Текущее количество hp: {self.health_keeper.health}"
        )
        self.parent_scene.get_audio_manager().load_sound("sceleton_hit")
        self.change_stage(Shadow.HIT)
        self.is_alert = True

    def check_death(self):
        if not self.health_keeper.is_died():
            return
        self.parent_scene.get_audio_manager().load_sound("sceleton_lose")
        self.change_stage(Shadow.DEAD)
        self.enable_updating = False

    def move_to(self, coordinates):
        ocx, ocy = coordinates
        scx, scy = self.get_centre_coordinates()

        if ocx < scx:
            self.move(-self.move_step, 0)
            if abs(ocx - scx) > 0.3:
                self.vertical_reverse = True
        else:
            self.move(self.move_step, 0)
            if abs(ocx - scx) > 0.3:
                self.vertical_reverse = False

        if ocy < scy:
            self.move(0, -self.move_step)
        else:
            self.move(0, self.move_step)

    def process_walking(self) -> bool:
        if self.current_stage == Shadow.REACT:
            return False
        if not self.is_alert:
            return False
        self.move_to(self.target_object.get_centre_coordinates())
        is_walking = True
        return is_walking

    def process_attacking(self) -> bool:
        is_attacking = False
        distance = self.get_distance_between_centres(self.target_object)
        if distance < self.start_attack_distance:
            if self.current_stage != Shadow.ATTACK:
                is_attacking = True
        return is_attacking

    def process_alert(self) -> bool:
        if self.target_object is None:
            return False
        if self.is_alert:
            return False
        if self.current_stage == Shadow.REACT:
            return False
        if self.alert_distance < self.get_distance_between_centres(self.target_object):
            return False
        self.parent_scene.get_scene_gui_manager().show_message("- Вас обнаружил Shadow")
        self.parent_scene.get_audio_manager().load_sound("sceleton_alert")
        return True

    def process_controller(self):
        if self.current_stage == Shadow.HIT:
            return
        if not self.enable_updating:
            return

        is_walking = self.process_walking()
        is_attacking = self.process_attacking()
        is_alert = self.process_alert()

        if is_walking:
            self.change_stage(Shadow.WALK)
        else:
            self.change_stage(Shadow.STAY)

        if is_attacking:
            self.change_stage(Shadow.ATTACK)
        if is_alert:
            self.change_stage(Shadow.REACT)

    def process_last_frame(self):
        if self.check_stage_end(Shadow.ATTACK):
            self.attack()
        if self.check_stage_end(Shadow.HIT):
            self.check_death()
        if self.check_stage_end(Shadow.REACT):
            self.is_alert = True

    def update(self):
        self.update_frame()
        self.process_last_frame()

    def draw(self, display_manager: GameVisualizer):
        display_manager.draw_image(
            "shadow", self.get_frame_code(),
            self.get_coordinates(),
            self.vertical_reverse
        )

    def draw_attention_zone(self, game_visualizer: GameVisualizer):
        if not self.is_alert:
            game_visualizer.draw_circle(
                *self.get_centre_coordinates(),
                self.alert_distance,
            )

    def draw_attack_zone(self, game_visualizer: GameVisualizer):
        game_visualizer.draw_circle(
            *self.get_centre_coordinates(),
            self.start_attack_distance,
            "orange"
        )
