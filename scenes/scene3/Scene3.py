import pygame

from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_game_logic.scene_folder.SceneDebug import SceneDebug
from scenes.scene1.scene_gui.GuiManagerScene1 import GuiManagerScene1
from scenes.scene3.game_objects.Player import Player
from scenes.scene3.game_objects.Shadow import Shadow
from scenes.scene3.general.rules import RULES
from scenes.scene3.general.scene_settings import OBJECTS_VISUALISATION, SCENE_AUDIO_PATHS
from scenes.scene3.map.Map import Map


class Scene3(SceneDebug):
    rules = RULES
    rules_text_font_size_coefficient = 1 / 20

    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        audio_manager.load_audio_data(SCENE_AUDIO_PATHS)
        self.game_visualizer.load_base_scaling_images(OBJECTS_VISUALISATION)
        self.scene_gui_manager = GuiManagerScene1(screen)
        self.scene_gui_manager.timer.start()
        self.show_debug_info = False

        self.map = Map()

        self.player = Player((6, 5),
                             OBJECTS_VISUALISATION["player"]["size"], self)
        self.player.set_moving_borders(self.map.border)

        self.enemies = [
            Shadow((7, 10), OBJECTS_VISUALISATION["shadow"]["size"], self),
            Shadow((5, 13), OBJECTS_VISUALISATION["shadow"]["size"], self),
            Shadow((11, 14), OBJECTS_VISUALISATION["shadow"]["size"], self),
        ]

        self.player.set_targets_to_attack(self.enemies.copy())

        for enemy in self.enemies:
            enemy.set_target_object(self.player)
            enemy.set_targets_to_attack([self.player])
            enemy.set_moving_borders(self.map.border)

        self.camera = self.game_visualizer.camera
        self.camera.fix_camera_on_object(self.player)

    def process_event(self, event: pygame.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:  # free camera mod
                self.game_visualizer.camera.switch_free_observing_mod()
                self.scene_gui_manager.show_message(
                    f"- camera: observing_mod = {self.game_visualizer.camera.is_free}"
                )
            elif event.key == pygame.K_p:
                self.show_debug_info = not self.show_debug_info
                self.scene_gui_manager.show_message(
                    f"- show_collisions = {self.show_debug_info}"
                )
        # self.process_debug_event(event)

    def update(self):
        for enemy in self.enemies:
            enemy.update()
            enemy.process_controller()
        self.player.update()
        if not self.get_game_visualizer().camera.is_free:
            self.player.process_controller()
        self.game_visualizer.update()
        self.scene_gui_manager.health_bar.update_health_bar(
            self.player.health_keeper.health, self.player.health_keeper.max_health)
        self.scene_gui_manager.stamina_bar.update_stamina_bar(
            self.player.stamina_keeper.current_stamina, self.player.stamina_keeper.max_stamina)
        self.scene_gui_manager.update()

    def draw(self):
        self.game_visualizer.refresh_screen()

        self.map.draw(self.game_visualizer)
        for enemy in self.enemies:
            enemy.draw(self.game_visualizer)
        self.player.draw(self.game_visualizer)

        if self.show_debug_info:
            self.draw_debug_info()
        # if self.show_grid:
        #     self.draw_grid()

        self.scene_gui_manager.draw()

    def draw_debug_info(self):
        self.map.draw_collisions(self.game_visualizer)
        self.player.draw_damage_area_collision(self.game_visualizer)
        self.player.draw_collision(self.game_visualizer)
        for enemy in self.enemies:
            enemy.draw_damage_area_collision(self.game_visualizer)
            enemy.draw_collision(self.game_visualizer)
            enemy.draw_attention_zone(self.game_visualizer)
            enemy.draw_attack_zone(self.game_visualizer)
