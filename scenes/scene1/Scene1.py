import pygame

from basic.Messanger import Messanger
from basic.game_logic.camera_folder.Camera import Camera
from basic.game_logic.collisions.damage_system.DamageController import DamageController
from basic.game_logic.layers_generator.LayersGenerator import LayersGenerator
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager
from basic.game_logic.visualization.GamingGuiManager import GamingGuiManager
from scenes.scene1.game_objects.loading_objects.loading_objects import *
from scenes.scene1.map.Map import Map


class Scene1:
    def __init__(self, screen, audio_manager):
        self.audio_manager = audio_manager
        self.messanger = Messanger()
        self.messanger.annotation_text = "Для продолжения нажмите на Enter..."
        self.messanger.end_key_code = 13  # enter
        self.gaming_gui_manager = GamingGuiManager()

        self.is_over = False
        self.current_stage = {
            "money_count": 0,
            "vase_count": 0,
            "key_count": 0
        }
        self.show_collisions = False
        self.enable_walls_collisions = True

        self.layers_map = LayersGenerator(width=15, height=15).get_layers()
        self.camera = Camera()
        self.display_manager = GamingDisplayManager(self.camera, screen)

        self.map = Map(self.layers_map[0])
        self.map.fill_collision_cells_map(self.layers_map["collision_map_scheme"])
        self.game_objects = get_objects(self.layers_map[2])
        self.player = self.game_objects.pop(get_player_index(self.game_objects))
        self.player.set_audio_manager(self.audio_manager)
        self.enemy = self.game_objects.pop(get_enemy_index(self.game_objects))
        self.enemy.set_target_object(self.player)
        self.enemy.set_map_collision_scheme(self.layers_map["collision_map_scheme"])
        self.enemy.set_audio_manager(self.audio_manager)
        self.enemy.set_gaming_gui_manager(self.gaming_gui_manager)

        self.camera.fix_camera_on_object(self.player)

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
                self.enable_walls_collisions = not self.enable_walls_collisions
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

    def keys_update(self):
        keys = pygame.key.get_pressed()

    def update(self):
        self.camera.update()
        self.keys_update()

    def clear_deleted_objects(self):
        for game_object_index in range(len(self.game_objects) - 1, -1, -1):
            game_object = self.game_objects[game_object_index]
            if game_object.is_deleted():
                self.game_objects.pop(game_object_index)

    def check_player_collisions(self):
        for game_object_index in range(len(self.game_objects) - 1, -1, -1):
            game_object = self.game_objects[game_object_index]
            if self.player.check_collision(game_object):
                code = game_object.get_code()
                if code == Money.CODE:
                    self.audio_manager.load_sound("coin")
                    game_object.delete()
                    self.current_stage["money_count"] += 1
                    self.gaming_gui_manager.add_item(code)
                    self.gaming_gui_manager.show_message(f"- Вы подобрали монету. Текущее количество: {self.current_stage["money_count"]}")
                elif code == Key.CODE:
                    self.audio_manager.load_sound("achievement")
                    game_object.delete()
                    self.current_stage["key_count"] += 1
                    self.gaming_gui_manager.add_item(code)
                    self.gaming_gui_manager.show_message(f"- Вы подобрали ключ. Найдите сундук для ключа")
                elif code == Vase.CODE and game_object.current_stage == Vase.CLOSED:
                    self.audio_manager.load_sound("coin")
                    game_object.collect()
                    self.current_stage["vase_count"] += 1
                    self.gaming_gui_manager.add_item(code)
                    self.gaming_gui_manager.show_message(f"- Вы подобрали вазу. Текущее количество: {self.current_stage["vase_count"]}")
                elif (code == Chess.CODE and self.current_stage["key_count"] == 1 and
                      game_object.current_stage == Chess.CLOSED):
                    self.audio_manager.load_sound("achievement")
                    game_object.open()

    def process_move(self, mover):
        if not self.enable_walls_collisions and isinstance(mover, Player):
            mover.do_move()
        else:
            mover.do_move(safe=True, hard_objects=self.map.get_near_walls(mover.get_centre_coordinates()))

    def process_enemy_attack(self):
        if self.enemy.request_damage_processing:
            self.enemy.request_damage_processing = False
            is_damaged, damage_impuls = DamageController.process_damage(self.enemy.damage_area, self.player)
            if is_damaged:
                damage = self.enemy.damage_area.damage
                self.player.process_getting_damage(damage)
                health = self.player.current_health
                if health < 0:
                    health = 0
                self.gaming_gui_manager.show_message(f"- Вы получили дамаг: {damage}. Текущее количество hp: {health}")
                self.audio_manager.load_sound("hero_hit")

    def process_player_attack(self):
        if self.player.request_damage_processing:
            self.player.request_damage_processing = False
            is_damaged, damage_impuls = DamageController.process_damage(self.player.damage_area, self.enemy)
            if is_damaged:
                damage = self.player.damage_area.damage
                self.enemy.process_getting_damage(damage)
                health = self.enemy.current_health
                if health < 0:
                    health = 0
                self.gaming_gui_manager.show_message(f"- Sceleton получил дамаг: {damage}. Текущее количество hp: {health}")
                self.audio_manager.load_sound("sceleton_hit")

    def check_win(self):
        for obj in self.game_objects:
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
        self.clear_deleted_objects()

        self.map.draw(self.display_manager)
        if self.show_collisions:
            self.map.draw_near_collisions(self.display_manager, self.player.get_centre_coordinates())

        for game_object in self.game_objects:
            game_object.update()
            game_object.draw(self.display_manager)
            if self.show_collisions:
                game_object.draw_collision(self.display_manager, game_object.get_code())

        self.enemy.update()
        self.process_move(self.enemy)
        self.process_enemy_attack()
        self.enemy.draw(self.display_manager)
        self.player.update()
        self.process_move(self.player)
        self.process_player_attack()
        self.player.draw(self.display_manager)
        if self.show_collisions:
            self.player.draw_collision(self.display_manager, self.player.get_code())
            self.enemy.draw_collision(self.display_manager, self.enemy.get_code())

        self.gaming_gui_manager.update()
        self.gaming_gui_manager.update_stamina_bar(self.player.current_stamina, self.player.max_stamina)
        self.gaming_gui_manager.update_health_bar(self.player.current_health, self.player.max_health)
        self.gaming_gui_manager.draw(screen)

        self.check_player_collisions()
        self.check_win()
        self.check_lose()
