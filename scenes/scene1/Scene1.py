import pygame

from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene1.map.loading_objects.loading_objects import *
from scenes.scene1.general.rules import RULES
from scenes.scene1.general.scene_settings import SCENE_AUDIO_PATHS, GAME_GUI_IMAGES
from scenes.scene1.map.Map import Map


class Scene1(Scene):
    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        self.audio_manager.load_audio_data(SCENE_AUDIO_PATHS)
        self.display_manager.load_images(OBJECTS_VISUALISATION)
        self.game_gui_manager.load_images(GAME_GUI_IMAGES)
        self.game_gui_manager.load_images(OBJECTS_VISUALISATION)

        self.is_over = False

        self.current_player_statistic = {"money_count": 0, "vase_count": 0, "key_count": 0}

        self.show_debug_info = False
        self.enable_walls_collisions = True

        self.map = Map(self)
        self.player = self.map.player
        self.enemy = self.map.enemy

        self.enemy.set_target_object(self.player)
        self.enemy.set_map_collision_scheme(self.map.collision_scheme)

        self.player.set_audio_manager(self.audio_manager)
        self.player.set_game_gui_manager(self.game_gui_manager)
        self.enemy.set_audio_manager(self.audio_manager)
        self.enemy.set_game_gui_manager(self.game_gui_manager)

        self.player.add_damage_processing_object(self.enemy)
        self.enemy.add_damage_processing_object(self.player)

        self.player.add_hard_objects(self.map.walls)
        self.enemy.add_hard_objects(self.map.walls)

        self.display_manager.get_camera().fix_camera_on_object(self.map.player)

    def get_rules(self):
        return RULES

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                self.game_gui_manager.switch_show_gui()
                if self.player.enable_updating:
                    self.display_manager.get_camera().enable_free_observing_mod()
                    self.player.enable_updating = False
                else:
                    self.display_manager.get_camera().fix_camera_on_object(self.player)
                    self.player.enable_updating = True
            elif event.key == pygame.K_p:
                self.show_debug_info = not self.show_debug_info
            elif event.key == pygame.K_i:
                self.player.set_collision_mode(not self.player.is_no_collision_mode())
            elif event.key == pygame.K_t:
                self.game_gui_manager.switch_timer()
            elif event.key == pygame.K_y:
                self.player.infinity_stamina = not self.player.infinity_stamina
            elif event.key == pygame.K_u:
                self.player.infinity_health = not self.player.infinity_health
            elif event.key == pygame.K_j:
                self.player.current_health = -1
            elif event.key == pygame.K_m:
                width, height = self.display_manager.get_screen().get_size()
                cur_scale = self.get_display_manager().size_tick_scale
                self.game_gui_manager.show_message(
                    f"screen size: {width}x{height}, size_tick_scale: {cur_scale}"
                )
            elif event.key == 45:  # "-"
                step = 5
                cur_scale = self.get_display_manager().size_tick_scale - step
                if cur_scale < step: cur_scale = step
                self.get_display_manager().set_size_tick_scale(cur_scale)
                self.get_display_manager().reload_images()
                self.game_gui_manager.show_message(f"size_tick_scale: {cur_scale}")
            elif event.key == 61:  # "+"
                step = 5
                cur_scale = self.get_display_manager().size_tick_scale + step
                self.get_display_manager().set_size_tick_scale(cur_scale)
                self.get_display_manager().reload_images()
                self.game_gui_manager.show_message(f"size_tick_scale: {cur_scale}")

    def check_player_collisions(self):
        for game_object in self.map.others:
            if self.player.check_collision(game_object):
                if isinstance(game_object, Money):
                    self.audio_manager.load_sound("coin")
                    game_object.delete()
                    self.current_player_statistic["money_count"] += 1
                    self.game_gui_manager.add_item("money")
                    self.game_gui_manager.show_message(
                        f"- Вы подобрали монету. Текущее количество: {self.current_player_statistic["money_count"]}")
                elif isinstance(game_object, Key):
                    self.audio_manager.load_sound("achievement")
                    game_object.delete()
                    self.current_player_statistic["key_count"] += 1
                    self.game_gui_manager.add_item("key")
                    self.game_gui_manager.show_message(f"- Вы подобрали ключ. Найдите сундук для ключа")
                elif isinstance(game_object, Vase) and game_object.current_stage == Vase.CLOSED:
                    self.audio_manager.load_sound("coin")
                    game_object.collect()
                    self.current_player_statistic["vase_count"] += 1
                    self.game_gui_manager.add_item("vase")
                    self.game_gui_manager.show_message(
                        f"- Вы подобрали вазу. Текущее количество: {self.current_player_statistic["vase_count"]}")
                elif (isinstance(game_object, Chess) and self.current_player_statistic["key_count"] == 1 and
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
                        self.display_manager.screen,
                        f"ПОБЕДА!\nрезультат: " +
                        f"\n-количество монет: {self.current_player_statistic["money_count"]}" +
                        f"\n-количество ваз: {self.current_player_statistic["vase_count"]}" +
                        f"\n-время: {self.game_gui_manager.get_timer_value()} секунд"
                    )
                    self.is_over = True

    def check_lose(self):
        if self.player.current_stage == Player.DEATH:
            self.audio_manager.to_pause()
            self.audio_manager.load_sound("lose")
            self.messanger.show_message(
                self.display_manager.screen,
                f"ПОРАЖЕНИЕ\nрезультат: " +
                f"\n-количество монет: {self.current_player_statistic["money_count"]}" +
                f"\n-количество ваз: {self.current_player_statistic["vase_count"]}" +
                f"\n-время: {self.game_gui_manager.get_timer_value()} секунд"
            )
            self.is_over = True

    def update(self):
        self.map.update()
        self.enemy.update()
        self.player.update()
        self.display_manager.update()
        self.game_gui_manager.update_stamina_bar(self.player.current_stamina, self.player.max_stamina)
        self.game_gui_manager.update_health_bar(self.player.current_health, self.player.max_health)
        self.game_gui_manager.update()
        self.check_player_collisions()
        self.check_win()
        self.check_lose()

    def draw(self):
        self.display_manager.refresh_screen()

        self.map.draw(self.display_manager)

        for game_object in self.map.others:
            game_object.update()
            game_object.draw(self.display_manager)

        self.enemy.draw(self.display_manager)
        self.player.draw(self.display_manager)

        if self.show_debug_info: self.draw_debug_info()
        self.game_gui_manager.draw(self.display_manager.get_screen())

    def draw_debug_info(self):
        self.map.draw_near_collisions(self.display_manager, self.player.get_centre_coordinates())
        self.map.draw_near_collisions(self.display_manager, self.enemy.get_centre_coordinates())
        for game_object in self.map.others:
            game_object.draw_collision(self.display_manager)
        self.player.draw_damage_area_collision(self.display_manager)
        self.enemy.draw_damage_area_collision(self.display_manager)
        self.player.draw_collision(self.display_manager)
        self.enemy.draw_collision(self.display_manager)
        self.enemy.draw_attention_zone(self.display_manager)
        self.enemy.draw_attack_zone(self.display_manager)
