import pygame

from basic.general_settings import FPS
from basic.general_game_logic.dynamic.damage_system.DamageArea import DamageArea
from basic.general_game_logic.base_objects.GameDynamicObject import GameDynamicObject
from basic.general_game_logic.visualization.GamingDisplayManager import GamingDisplayManager


class Player(GameDynamicObject):
    ATTACK, STAY, DEAD, DEATH, WALK, RUN, HIT = "attack", "stay", "dead", "death", "walk", "run", "hit"
    frames = {
        ATTACK: ["attack1", "attack2", "attack3", "attack4", "attack5", "attack4", "attack3", "attack2"],
        STAY: ["attack1"],
        DEAD: ["dead1", "dead2", "dead3", "dead4", "dead5", "dead6"],
        DEATH: ["dead6"],
        WALK: ["walk1", "walk2", "walk3", "walk4", "walk5"],
        RUN: ["run1", "run2", "run3", "run4", "run5", "run6", "run7"],
        HIT: ["hit1", "hit2", "hit1"]
    }
    frames_per_second = {
        ATTACK: 12,
        STAY: 5,
        DEAD: 5,
        DEATH: 5,
        WALK: 5,
        RUN: 5,
        HIT: 3
    }
    long_term_stages = (ATTACK, DEAD, HIT)

    def __init__(self, coordinates, size=(0, 0)):
        super().__init__(coordinates, size)
        self.create_collision_rect(0.35, -0.3, 0.3, 0.6)
        self.audio_manager = None
        self.gaming_gui_manager = None
        self.current_stage = Player.STAY
        self.enable_updating = True

        # Characteristics
        self.move_step = 0.02
        self.run_step = 0.05
        self.max_stamina = 100
        self.current_stamina = 100
        self.decrease_stamina_speed = 20  # per second
        self.increase_stamina_speed = 10  # per second
        self.min_running_stamina_level = 20
        self.infinity_stamina = False

        self.attack_delay = 0.9  # sec
        self.current_attack_delay = 0

        self.damage_area = DamageArea((0, 0), rect=(0.1, -0.3, 0.8, 0.6))
        self.damage = 20
        self.max_health = 100
        self.current_health = 100
        self.infinity_health = False

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

    def update_stamina(self):
        if self.current_stamina < 0:
            self.current_stamina = 0
        self.current_stamina += self.increase_stamina_speed / FPS
        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    def process_running(self):
        is_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and (
                self.current_stamina > self.min_running_stamina_level or self.infinity_stamina
        ):
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

    def process_walking(self):
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

    def process_attacking(self):
        keys = pygame.key.get_pressed()
        is_attacking = False
        if keys[pygame.K_e] and self.current_attack_delay == 0:
            self.current_attack_delay = self.attack_delay
            is_attacking = True
        return is_attacking

    def process_getting_damage(self, damage):
        self.decrease_health(damage)
        if self.current_stage != Player.DEAD:
            self.current_stage = Player.HIT
            self.set_stage_updating_delay()
            self.gaming_gui_manager.show_message(
                f"- Вы получили дамаг: {damage}. Текущее количество hp: {self.current_health}"
            )
            self.audio_manager.load_sound("hero_hit")

    def check_death(self):
        if self.current_health <= 0 and not self.infinity_health:
            self.load_sound_safety("death")
            self.current_stage = Player.DEAD
            self.set_stage_updating_delay()
            self.enable_updating = False

    def process_controller(self):
        self.current_attack_delay -= 1 / FPS
        if self.current_attack_delay < 0:
            self.current_attack_delay = 0

        if self.current_stage == Player.HIT:
            return

        is_walking = self.process_walking()
        is_running = self.process_running()
        is_attacking = self.process_attacking()

        self.update_stages(Player.STAY)
        if is_walking:
            self.update_stages(Player.WALK)
        if is_running:
            self.update_stages(Player.RUN)
            self.current_stamina -= self.decrease_stamina_speed / FPS
            if self.current_stamina < self.min_running_stamina_level:
                self.current_stamina = 0
        if is_attacking:
            self.update_stages(Player.ATTACK)

    def set_stage_updating_delay(self):
        if self.current_stage in Player.long_term_stages:
            self.current_frame_index = 0
            self.stage_updating_delay = len(Player.frames[self.current_stage]) - 1

    def update_stages(self, new_stage=None):
        if not self.stage_updating_delay:
            if self.current_stage == Player.DEAD:
                self.current_stage = Player.DEATH
            elif self.current_stage == Player.ATTACK:
                self.current_stage = Player.STAY
                self.do_damage()
            elif self.current_stage == Player.HIT:
                self.current_stage = Player.STAY
            elif new_stage is not None:
                self.current_stage = new_stage
                if self.current_stage in Player.long_term_stages:
                    self.set_stage_updating_delay()

    def update(self):
        if self.enable_updating:
            self.process_controller()
            self.update_stamina()
            self.check_death()
        self.update_stages()
        self.update_frame()

    def draw(self, display_manager: GamingDisplayManager):
        display_manager.draw_image(
            "hero", Player.frames[self.current_stage][self.current_frame_index],
            self.get_coordinates(),
            self.vertical_reverse
        )
