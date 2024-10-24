from basic.general_settings import FPS
from basic.general_game_logic.dynamic.damage_system.DamageArea import DamageArea
from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.base_objects.GameDynamicObject import GameDynamicObject
from basic.general_game_logic.visualization.GamingDisplayManager import GamingDisplayManager
from scenes.scene1.map.layers_generator.maze.maze_solver import bfs
from scenes.scene1.map.layers_generator.get_scheme_coordinates import get_scheme_coordinates


class Sceleton(GameDynamicObject):
    ATTACK, STAY, DEAD, DEATH, WALK, HIT, REACT = "attack", "stay", "dead", "death", "walk", "hit", "react"
    frames = {
        ATTACK: ["attack1", "attack2", "attack3", "attack4", "attack5", "attack6",
                 "attack7", "attack8", "attack9", "attack10", "attack11", "attack12"],
        STAY: ["idle1", "idle2", "idle3", "idle4", "idle5", "idle6", "idle7", "idle8", "idle9", "idle10", "idle11"],
        DEAD: ["dead1", "dead2", "dead3", "dead4", "dead5", "dead6", "dead7", "dead8", "dead9", "dead10", "dead11",
               "dead12", "dead13", "dead14", "dead15"],
        DEATH: ["dead15"],
        WALK: ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6", "walk7", "walk8", "walk9",
               "walk10", "walk11", "walk12", "walk13"],
        HIT: ["hit1", "hit2", "hit3", "hit4", "hit5", "hit6", "hit7", "hit8"],
        REACT: ["react1", "react2", "react3", "react4", "react1", "react2", "react3", "react4"]
    }
    frames_per_second = {
        ATTACK: 12,
        STAY: 6,
        DEAD: 4,
        DEATH: 3,
        WALK: 16,
        HIT: 10,
        REACT: 2
    }
    long_term_stages = (ATTACK, DEAD, REACT, HIT)

    def __init__(self, coordinates, size):
        super().__init__(coordinates, size)
        self.create_collision_rect(0.14, -0.15, 0.42, 0.55)
        self.audio_manager = None
        self.gaming_gui_manager = None
        self.current_stage = Sceleton.STAY
        self.enable_updating = True

        # Characteristics
        self.move_step = 0.02
        self.run_step = 0.05
        self.attack_delay = 2  # sec
        self.current_attack_delay = 0
        self.current_attack_distance = 0.8
        self.alert_distance = 3  # ticks
        self.is_alert = False

        self.damage_area = DamageArea((0, 0), rect=(0, 0, 0.7, 0.7))
        self.damage = 34
        self.max_health = 100
        self.current_health = 100
        self.infinity_health = False

        # Enemy parameters
        self.target_object = None
        self.map_collision_scheme = None

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
            self.current_time = 1 / Sceleton.frames_per_second[self.current_stage]  # sec
            self.current_frame_index += 1
            if self.stage_updating_delay > 0:
                self.stage_updating_delay -= 1
        self.current_frame_index %= len(Sceleton.frames[self.current_stage])

    def set_target_object(self, obj: GameObject):
        self.target_object = obj

    def set_map_collision_scheme(self, map_collision_scheme):
        self.map_collision_scheme = map_collision_scheme

    def process_alert(self):
        if self.target_object is not None:
            if not self.is_alert:
                distance = self.get_distance_between_centres(self.target_object)
                if self.alert_distance > distance:
                    self.is_alert = True
                    self.show_message_safety("- Вас обнаружил Sceleton")
                    self.load_sound_safety("sceleton_alert")
                    self.update_stages(Sceleton.REACT)

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

    def process_walking(self):
        if self.current_stage != Sceleton.REACT and self.is_alert:
            distance = self.get_distance_between_centres(self.target_object)
            if distance < 1:
                self.move_to(self.target_object.get_centre_coordinates())
                self.update_stages(Sceleton.WALK)
            else:
                scheme_self_coordinates = get_scheme_coordinates(self.get_centre_coordinates())
                scheme_obj_coordinates = get_scheme_coordinates(self.target_object.get_centre_coordinates())
                if self.is_free_cell(scheme_self_coordinates) and self.is_free_cell(scheme_obj_coordinates):
                    path = bfs(self.map_collision_scheme, scheme_self_coordinates, scheme_obj_coordinates)
                    if len(path) > 1:
                        row, col = path[1]
                        self.move_to((col + 0.5, row - 0.5))
                        self.update_stages(Sceleton.WALK)

    def process_attacking(self):
        distance = self.get_distance_between_centres(self.target_object)
        if distance < self.current_attack_distance and self.current_attack_delay == 0:
            self.update_stages(Sceleton.ATTACK)

    def process_getting_damage(self, damage):
        self.decrease_health(damage)
        self.is_alert = True
        if self.current_stage != Sceleton.DEAD:
            self.current_stage = Sceleton.HIT
            self.set_stage_updating_delay()
            self.gaming_gui_manager.show_message(
                f"- Sceleton получил дамаг: {damage}. Текущее количество hp: {self.current_health}"
            )
            self.audio_manager.load_sound("sceleton_hit")

    def check_death(self):
        if self.current_health <= 0 and not self.infinity_health:
            self.current_stage = Sceleton.DEAD
            self.set_stage_updating_delay()
            self.enable_updating = False
            self.load_sound_safety("sceleton_lose")

    def process_controller(self):
        self.current_attack_delay -= 1 / FPS
        if self.current_attack_delay < 0:
            self.current_attack_delay = 0

        self.update_stages(Sceleton.STAY)
        if self.current_stage != Sceleton.HIT:
            self.process_walking()
            self.process_attacking()
        self.process_alert()

    def set_stage_updating_delay(self):
        if self.current_stage in Sceleton.long_term_stages:
            self.current_frame_index = 0
            self.stage_updating_delay = len(Sceleton.frames[self.current_stage]) - 1

    def update_stages(self, new_stage=None):
        if not self.stage_updating_delay:
            if self.current_stage == Sceleton.DEAD:
                self.current_stage = Sceleton.DEATH
            elif self.current_stage == Sceleton.ATTACK:
                self.current_stage = Sceleton.STAY
                self.do_damage()
            elif self.current_stage == Sceleton.REACT:
                self.current_stage = Sceleton.STAY
                self.show_message_safety("- Sceleton начал охоту на вас")
            elif self.current_stage == Sceleton.HIT:
                self.current_stage = Sceleton.STAY
            elif new_stage is not None:
                self.current_stage = new_stage
                if self.current_stage in Sceleton.long_term_stages:
                    self.set_stage_updating_delay()

    def update(self):
        if self.enable_updating:
            self.process_controller()
            self.check_death()
        self.update_stages()
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image(
            "sceleton", Sceleton.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates(),
            self.vertical_reverse
        )

    def draw_attention_zone(self, display_manager: GamingDisplayManager):
        if not self.is_alert:
            display_manager.draw_circle(
                *self.get_centre_coordinates(),
                self.alert_distance,
            )

    def draw_attack_zone(self, display_manager: GamingDisplayManager):
        display_manager.draw_circle(
            *self.get_centre_coordinates(),
            self.current_attack_distance,
            "orange"
        )
