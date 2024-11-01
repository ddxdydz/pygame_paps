import pygame

from basic.general_game_logic.scene_folder.Scene import Scene
from scenes.scene3.game_objects.Player import Player
from scenes.scene3.general.rules import RULES
from scenes.scene3.general.scene_settings import OBJECTS_VISUALISATION
from scenes.scene3.map.Map import Map


class Scene3(Scene):
    rules = RULES
    rules_text_font_size_coefficient = 1 / 20

    def __init__(self, screen, audio_manager):
        super().__init__(screen, audio_manager)
        self.game_visualizer.load_base_scaling_images(OBJECTS_VISUALISATION)
        self.show_debug_info = False
        self.scaling_step = 20

        self.map = Map()

        self.player = Player((self.map.width // 4, self.map.height // 2),
                             OBJECTS_VISUALISATION["player"]["size"], self)
        self.player.set_moving_borders(self.map.border)

        self.camera = self.game_visualizer.camera
        self.camera.fix_camera_on_object(self.player)

        self.input_points = []

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

    def update(self):
        self.player.update()
        if not self.get_game_visualizer().camera.is_free:
            self.player.process_controller()
        self.game_visualizer.update()
        self.scene_gui_manager.update()

    def draw(self):
        self.game_visualizer.refresh_screen()

        self.map.draw(self.game_visualizer)
        self.player.draw(self.game_visualizer)

        if self.show_debug_info:
            self.draw_debug_info()

        self.scene_gui_manager.draw()

    def draw_debug_info(self):
        self.map.draw_collisions(self.game_visualizer)
        self.player.draw_collision(self.game_visualizer)
