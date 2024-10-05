import pygame

from basic.Messanger import Messanger
from basic.game_logic.camera_folder.Camera import Camera
from basic.game_logic.collisions.CollisionController import CollisionController
from basic.game_logic.layers_generator.LayersGenerator import LayersGenerator
from basic.game_logic.visualization.GamingDisplayManager import GamingDisplayManager
from scenes.scene1.game_objects.loading_objects.loading_objects import *
from scenes.scene1.map.Map import Map


class Scene1:
    def __init__(self, screen, audio_manager):
        self.audio_manager = audio_manager
        self.messanger = Messanger()
        self.messanger.annotation_text = "Для продолжения нажмите на Enter..."
        self.messanger.end_key_code = 13  # enter

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

        self.camera.fix_camera_on_object(self.player)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
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
                    self.audio_manager.load_coin_sound()
                    game_object.delete()
                    self.current_stage["money_count"] += 1
                elif code == Key.CODE:
                    self.audio_manager.load_achievement_sound()
                    game_object.delete()
                    self.current_stage["key_count"] += 1
                elif code == Vase.CODE and game_object.current_stage == Vase.CLOSED:
                    self.audio_manager.load_coin_sound()
                    game_object.collect()
                    self.current_stage["vase_count"] += 1
                elif (code == Chess.CODE and self.current_stage["key_count"] == 1 and
                      game_object.current_stage == Chess.CLOSED):
                    self.audio_manager.load_achievement_sound()
                    game_object.open()

    def process_move(self, mover):
        if self.enable_walls_collisions:
            mover.do_move(safe=True, hard_objects=self.map.get_near_walls(mover.get_centre_coordinates()))
        else:
            mover.do_move()

    def check_win(self):
        for obj in self.game_objects:
            if isinstance(obj, Chess):
                if obj.current_stage == Chess.OPENED:
                    self.audio_manager.to_pause()
                    self.audio_manager.load_win_sound()
                    self.messanger.show_message(
                        f"ПОБЕДА!\nрезультат: \n-количество монет: {self.current_stage["money_count"]}\n-количество ваз: {self.current_stage["vase_count"]}",
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

        self.player.update()
        self.process_move(self.player)
        self.player.draw(self.display_manager)
        if self.show_collisions:
            self.player.draw_collision(self.display_manager, self.player.get_code())

        self.check_player_collisions()
        self.check_win()
