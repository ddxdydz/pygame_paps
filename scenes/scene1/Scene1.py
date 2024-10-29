import pygame

from basic.audio.AudioManager import AudioManager
from basic.general_game_logic.scene_folder.SceneDebug import SceneDebug
from scenes.scene1.game_objects.Chess import Chess
from scenes.scene1.game_objects.Key import Key
from scenes.scene1.game_objects.Money import Money
from scenes.scene1.game_objects.Player import Player
from scenes.scene1.game_objects.Vase import Vase
from scenes.scene1.general.rules import RULES
from scenes.scene1.general.scene_settings import OBJECTS_VISUALISATION, SCENE_AUDIO_PATHS
from scenes.scene1.map.Map import Map
from scenes.scene1.scene_gui.GuiManagerScene1 import GuiManagerScene1


class Scene1(SceneDebug):
    rules = RULES

    def __init__(self, screen, audio_manager: AudioManager = AudioManager()):
        super().__init__(screen, audio_manager)
        audio_manager.load_audio_data(SCENE_AUDIO_PATHS)
        self.game_visualizer.load_base_scaling_images(OBJECTS_VISUALISATION)
        self.scene_gui_manager = GuiManagerScene1(screen)
        self.scene_gui_manager.timer.start()

        self.current_player_statistic = {"money_count": 0, "vase_count": 0, "key_count": 0}

        self.map = Map(self)
        self.player = self.map.player
        self.enemy = self.map.enemy

        self.enemy.set_target_object(self.player)
        self.enemy.set_map_collision_scheme(self.map.collision_scheme)

        self.player.set_audio_manager(self.audio_manager)
        self.player.set_game_gui_manager(self.scene_gui_manager)
        self.enemy.set_audio_manager(self.audio_manager)
        self.enemy.set_game_gui_manager(self.scene_gui_manager)

        self.player.add_damage_processing_object(self.enemy)
        self.enemy.add_damage_processing_object(self.player)

        self.player.add_hard_objects(self.map.walls)
        self.enemy.add_hard_objects(self.map.walls)

        self.game_visualizer.get_camera().fix_camera_on_object(self.map.player)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                self.player.set_collision_mode(not self.player.is_no_collision_mode())
            elif event.key == pygame.K_y:
                self.player.infinity_stamina = not self.player.infinity_stamina
            elif event.key == pygame.K_u:
                self.player.infinity_health = not self.player.infinity_health
            elif event.key == pygame.K_j:
                self.player.current_health = -1
            elif event.key == pygame.K_t:
                pass
        self.process_debug_event(event)

    def check_player_collisions(self):
        for game_object in self.map.others:
            if self.player.check_collision(game_object):
                if isinstance(game_object, Money):
                    self.audio_manager.load_sound("coin")
                    game_object.delete()
                    self.current_player_statistic["money_count"] += 1
                    self.scene_gui_manager.items_panel.add_item("money")
                    self.scene_gui_manager.show_message(
                        f"- Вы подобрали монету. Текущее количество: {self.current_player_statistic["money_count"]}")
                elif isinstance(game_object, Key):
                    self.audio_manager.load_sound("achievement")
                    game_object.delete()
                    self.current_player_statistic["key_count"] += 1
                    self.scene_gui_manager.items_panel.add_item("key")
                    self.scene_gui_manager.show_message(f"- Вы подобрали ключ. Найдите сундук для ключа")
                elif isinstance(game_object, Vase) and game_object.current_stage == Vase.CLOSED:
                    self.audio_manager.load_sound("coin")
                    game_object.collect()
                    self.current_player_statistic["vase_count"] += 1
                    self.scene_gui_manager.items_panel.add_item("vase")
                    self.scene_gui_manager.show_message(
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
                        self.game_visualizer.screen,
                        f"ПОБЕДА!\nрезультат: " +
                        f"\n-количество монет: {self.current_player_statistic["money_count"]}" +
                        f"\n-количество ваз: {self.current_player_statistic["vase_count"]}" +
                        f"\n-время: {self.scene_gui_manager.timer.get_time()} секунд"
                    )
                    self.is_over = True

    def check_lose(self):
        if self.player.current_stage == Player.DEATH:
            self.audio_manager.to_pause()
            self.audio_manager.load_sound("lose")
            self.messanger.show_message(
                self.game_visualizer.screen,
                f"ПОРАЖЕНИЕ\nрезультат: " +
                f"\n-количество монет: {self.current_player_statistic["money_count"]}" +
                f"\n-количество ваз: {self.current_player_statistic["vase_count"]}" +
                f"\n-время: {self.scene_gui_manager.timer.get_time()} секунд"
            )
            self.is_over = True

    def update(self):
        self.map.update()
        self.enemy.update()
        self.player.update()
        self.game_visualizer.update()
        self.scene_gui_manager.health_bar.update_health_bar(self.player.current_health, self.player.max_health)
        self.scene_gui_manager.stamina_bar.update_stamina_bar(self.player.current_stamina, self.player.max_stamina)
        self.scene_gui_manager.update()
        self.check_player_collisions()
        self.check_win()
        self.check_lose()

    def draw(self):
        self.game_visualizer.refresh_screen()

        self.map.draw(self.game_visualizer)
        for game_object in self.map.others:
            game_object.update()
            game_object.draw(self.game_visualizer)
        self.enemy.draw(self.game_visualizer)
        self.player.draw(self.game_visualizer)

        if self.show_debug_info:
            self.draw_debug_info()

        self.scene_gui_manager.draw()

    def draw_debug_info(self):
        self.map.draw_near_collisions(self.game_visualizer, self.player.get_centre_coordinates())
        self.map.draw_near_collisions(self.game_visualizer, self.enemy.get_centre_coordinates())
        for game_object in self.map.others:
            game_object.draw_collision(self.game_visualizer)
        self.player.draw_damage_area_collision(self.game_visualizer)
        self.enemy.draw_damage_area_collision(self.game_visualizer)
        self.player.draw_collision(self.game_visualizer)
        self.enemy.draw_collision(self.game_visualizer)
        self.enemy.draw_attention_zone(self.game_visualizer)
        self.enemy.draw_attack_zone(self.game_visualizer)
