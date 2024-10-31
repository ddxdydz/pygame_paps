from math import inf

from basic.general_game_logic.base_objects.GameAnimatedObject import GameAnimatedObject
from basic.general_game_logic.base_objects.GameCombatObject import GameCombatObject
from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.collision_system.rectangle_collision.CollisionRect import CollisionRect
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene1.general.scene_settings import SCELETON_ANIMATION
from scenes.scene1.map.layers_generator.get_scheme_coordinates import get_scheme_coordinates
from scenes.scene1.map.layers_generator.maze.maze_solver import bfs


class Sceleton(GameCombatObject, GameAnimatedObject):
    ATTACK, STAY, DEAD, DEATH, WALK, HIT, REACT = SCELETON_ANIMATION.keys()

    def __init__(self, coordinates, size, parent_scene: Scene):
        super().__init__(coordinates, size)
        GameAnimatedObject.__init__(self, self.STAY, SCELETON_ANIMATION)
        self.parent_scene = parent_scene
        self.create_collision_rect(0.14, -0.15, 0.42, 0.55)
        self.vertical_reverse = False
        self.enable_updating = True

        # Moving
        self.move_step = 0.02
        self.run_step = 0.05

        # Combat Parameters
        self.set_damage_parameters(CollisionRect(0, 0, 0.7, 0.7), 34)
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

    def set_map_collision_scheme(self, map_collision_scheme):
        self.map_collision_scheme = map_collision_scheme

    def take_hit(self, damage):
        if self.health_keeper.health == 0:
            return
        self.health_keeper.take_damage(damage)
        self.parent_scene.get_scene_gui_manager().show_message(
            f"- Sceleton получил дамаг: {damage}. Текущее количество hp: {self.health_keeper.health}"
        )
        self.parent_scene.get_audio_manager().load_sound("sceleton_hit")
        self.change_stage(Sceleton.HIT)
        self.is_alert = True

    def check_death(self):
        if not self.health_keeper.is_died():
            return
        self.parent_scene.get_audio_manager().load_sound("sceleton_lose")
        self.change_stage(Sceleton.DEAD)
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

    def is_free_cell(self, scheme_coordinates):
        row, col = scheme_coordinates
        height, width = len(self.map_collision_scheme), len(self.map_collision_scheme[0])
        if -1 < row < height and -1 < col < width:
            if not self.map_collision_scheme[row][col]:
                return True
        return False

    def get_next_cell_coordinates(self) -> tuple[float, float]:
        self_scheme_coordinates = get_scheme_coordinates(self.get_centre_coordinates())
        obj_scheme_coordinates = get_scheme_coordinates(self.target_object.get_centre_coordinates())
        if self.is_free_cell(self_scheme_coordinates) and self.is_free_cell(obj_scheme_coordinates):
            path = bfs(self.map_collision_scheme, self_scheme_coordinates, obj_scheme_coordinates)
            if len(path) > 1:
                return path[1]
        return inf, inf

    def process_walking(self) -> bool:
        if self.current_stage == Sceleton.REACT:
            return False
        if not self.is_alert:
            return False
        is_walking = False
        distance = self.get_distance_between_centres(self.target_object)
        if distance < 1:
            self.move_to(self.target_object.get_centre_coordinates())
            is_walking = True
        else:
            row, col = self.get_next_cell_coordinates()
            if row != inf:
                self.move_to((col + 0.5, row - 0.5))
                is_walking = True
        return is_walking

    def process_attacking(self) -> bool:
        is_attacking = False
        distance = self.get_distance_between_centres(self.target_object)
        if distance < self.start_attack_distance:
            if self.current_stage != Sceleton.ATTACK:
                is_attacking = True
        return is_attacking

    def process_alert(self) -> bool:
        if self.target_object is None:
            return False
        if self.is_alert:
            return False
        if self.current_stage == Sceleton.REACT:
            return False
        if self.alert_distance < self.get_distance_between_centres(self.target_object):
            return False
        self.parent_scene.get_scene_gui_manager().show_message("- Вас обнаружил Sceleton")
        self.parent_scene.get_audio_manager().load_sound("sceleton_alert")
        return True

    def process_controller(self):
        if self.current_stage == Sceleton.HIT:
            return
        if not self.enable_updating:
            return

        is_walking = self.process_walking()
        is_attacking = self.process_attacking()
        is_alert = self.process_alert()

        if is_walking:
            self.change_stage(Sceleton.WALK)
        else:
            self.change_stage(Sceleton.STAY)

        if is_attacking:
            self.change_stage(Sceleton.ATTACK)
        if is_alert:
            self.change_stage(Sceleton.REACT)

    def process_last_frame(self):
        if self.check_stage_end(Sceleton.ATTACK):
            self.attack()
        if self.check_stage_end(Sceleton.HIT):
            self.check_death()
        if self.check_stage_end(Sceleton.REACT):
            self.is_alert = True

    def update(self):
        self.update_frame()
        self.process_last_frame()

    def draw(self, display_manager: GameVisualizer):
        display_manager.draw_image(
            "sceleton", self.get_frame_code(),
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
