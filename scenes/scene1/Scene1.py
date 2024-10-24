import pygame

from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene1.general.loading_objects.loading_objects import *
from scenes.scene1.general.scene_settings import SCENE_AUDIO_PATHS
from scenes.scene1.map.Map import Map


class Scene1(Scene):
    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        self.audio_manager.load_audio_data(SCENE_AUDIO_PATHS)
        self.display_manager.load_images(OBJECTS_VISUALISATION)

        self.is_over = False

        self.current_stage = {
            "money_count": 0,
            "vase_count": 0,
            "key_count": 0
        }

        self.show_collisions = False
        self.enable_walls_collisions = True

        self.map = Map()
        self.player = self.map.player
        self.enemy = self.map.enemy

        self.enemy.set_target_object(self.player)
        self.enemy.set_map_collision_scheme(self.map.collision_scheme)

        self.player.set_audio_manager(self.audio_manager)
        self.player.set_gaming_gui_manager(self.gaming_gui_manager)
        self.enemy.set_audio_manager(self.audio_manager)
        self.enemy.set_gaming_gui_manager(self.gaming_gui_manager)

        self.player.add_damage_processing_object(self.enemy)
        self.enemy.add_damage_processing_object(self.player)

        self.player.add_hard_objects(self.map.walls)
        self.enemy.add_hard_objects(self.map.walls)

        self.camera.fix_camera_on_object(self.map.player)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                self.gaming_gui_manager.switch_show_gui()
                if self.camera.is_free:
                    self.camera.fix_camera_on_object(self.player)
                    self.player.enable_updating = True
                else:
                    self.camera.enable_free_observing_mod()
                    self.player.enable_updating = False
            elif event.key == pygame.K_p:
                self.show_collisions = not self.show_collisions
            elif event.key == pygame.K_i:
                self.player.set_collision_mode(not self.player.is_no_collision_mode())
            elif event.key == pygame.K_t:
                self.gaming_gui_manager.switch_timer()
            elif event.key == pygame.K_y:
                self.player.infinity_stamina = not self.player.infinity_stamina
            elif event.key == pygame.K_u:
                self.player.infinity_health = not self.player.infinity_health
            elif event.key == pygame.K_j:
                self.player.current_health = -1
            elif event.key == pygame.K_m:
                self.gaming_gui_manager.show_message("Test MESSAGE")

    def update(self):
        self.camera.update()

    def check_player_collisions(self):
        for game_object in self.map.others:
            if self.player.check_collision(game_object):
                if isinstance(game_object, Money):
                    self.audio_manager.load_sound("coin")
                    game_object.delete()
                    self.current_stage["money_count"] += 1
                    self.gaming_gui_manager.add_item("money")
                    self.gaming_gui_manager.show_message(
                        f"- Вы подобрали монету. Текущее количество: {self.current_stage["money_count"]}")
                elif isinstance(game_object, Key):
                    self.audio_manager.load_sound("achievement")
                    game_object.delete()
                    self.current_stage["key_count"] += 1
                    self.gaming_gui_manager.add_item("key")
                    self.gaming_gui_manager.show_message(f"- Вы подобрали ключ. Найдите сундук для ключа")
                elif isinstance(game_object, Vase) and game_object.current_stage == Vase.CLOSED:
                    self.audio_manager.load_sound("coin")
                    game_object.collect()
                    self.current_stage["vase_count"] += 1
                    self.gaming_gui_manager.add_item("vase")
                    self.gaming_gui_manager.show_message(
                        f"- Вы подобрали вазу. Текущее количество: {self.current_stage["vase_count"]}")
                elif (isinstance(game_object, Chess) and self.current_stage["key_count"] == 1 and
                      game_object.current_stage == Chess.CLOSED):
                    self.audio_manager.load_sound("achievement")
                    game_object.open()

    def check_win(self):
        for obj in self.map.others:
            if isinstance(obj, Chess):
                if obj.current_stage == Chess.OPENED:
                    self.audio_manager.to_pause()
                    self.audio_manager.load_sound("win")
                    self.messanger.show_message(
                        f"ПОБЕДА!\nрезультат: " +
                        f"\n-количество монет: {self.current_stage["money_count"]}" +
                        f"\n-количество ваз: {self.current_stage["vase_count"]}" +
                        f"\n-время: {self.gaming_gui_manager.get_timer_value()} секунд",
                        self.display_manager.screen
                    )
                    self.is_over = True

    def check_lose(self):
        if self.player.current_stage == Player.DEATH:
            self.audio_manager.to_pause()
            self.audio_manager.load_sound("lose")
            self.messanger.show_message(
                f"ПОРАЖЕНИЕ\nрезультат: " +
                f"\n-количество монет: {self.current_stage["money_count"]}" +
                f"\n-количество ваз: {self.current_stage["vase_count"]}" +
                f"\n-время: {self.gaming_gui_manager.get_timer_value()} секунд",
                self.display_manager.screen
            )
            self.is_over = True

    def draw(self, screen):
        self.display_manager.update_screen(screen)
        self.map.update()

        self.map.draw(self.display_manager)
        if self.show_collisions:
            self.map.draw_near_collisions(self.display_manager, self.player.get_centre_coordinates())

        for game_object in self.map.others:
            game_object.update()
            game_object.draw(self.display_manager)
            if self.show_collisions:
                game_object.draw_collision(self.display_manager)

        self.enemy.update()
        self.enemy.draw(self.display_manager)
        self.player.update()
        self.player.draw(self.display_manager)
        if self.show_collisions:
            self.player.draw_damage_area_collision(self.display_manager)
            self.enemy.draw_damage_area_collision(self.display_manager)
            self.player.draw_collision(self.display_manager)
            self.enemy.draw_collision(self.display_manager)
            self.enemy.draw_attention_zone(self.display_manager)
            self.enemy.draw_attack_zone(self.display_manager)

        self.gaming_gui_manager.update()
        self.gaming_gui_manager.update_stamina_bar(self.player.current_stamina, self.player.max_stamina)
        self.gaming_gui_manager.update_health_bar(self.player.current_health, self.player.max_health)
        self.gaming_gui_manager.draw(screen)

        self.check_player_collisions()
        self.check_win()
        self.check_lose()
