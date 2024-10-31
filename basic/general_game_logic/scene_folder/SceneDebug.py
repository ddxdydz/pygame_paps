import pygame

from basic.audio.AudioManager import AudioManager
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.tools.draw_tools.Grid import Grid
from basic.tools.draw_tools.draw_mouse_game_coordinates import draw_mouse_game_coordinates


class SceneDebug(Scene):
    def __init__(self, screen, audio_manager: AudioManager()):
        super().__init__(screen, audio_manager)
        self.show_debug_info = False
        self.show_grid = False
        self.scaling_step = 5

    def switch_show_debug_info(self):
        self.show_debug_info = not self.show_debug_info

    def switch_show_grid(self):
        self.show_grid = not self.show_grid

    def process_debug_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:  # free camera mod
                self.scene_gui_manager.switch_show_gui()
                self.game_visualizer.camera.switch_free_observing_mod()
                self.scene_gui_manager.show_message(
                    f"- camera: observing_mod = {self.game_visualizer.camera.is_free}"
                )
            elif event.key == pygame.K_v:
                self.scene_gui_manager.switch_show_gui()
                self.scene_gui_manager.show_message(
                    f"- gui: show = {self.scene_gui_manager.show_gui}"
                )
            elif event.key == pygame.K_p:
                self.show_debug_info = not self.show_debug_info
                self.scene_gui_manager.show_message(
                    f"- show_debug_info = {self.show_debug_info}"
                )
            elif event.key == pygame.K_g:
                self.show_grid = not self.show_grid
                self.scene_gui_manager.show_message(f"- show_grid = {self.show_grid}")
            elif event.key == pygame.K_r:
                self.auto_size()
            elif event.key == pygame.K_m:
                width, height = self.game_visualizer.get_screen().get_size()
                cur_scale = self.get_game_visualizer().get_current_tick_size()
                self.scene_gui_manager.show_message(
                    f"- screen size: {width}x{height}, size_tick_scale: {cur_scale}"
                )
            elif event.key == 45:  # "-"
                self.get_game_visualizer().decrease_current_tick_size(self.scaling_step)
                self.scene_gui_manager.show_message(
                    f"- size_tick_scale: {self.get_game_visualizer().get_current_tick_size()}"
                )
            elif event.key == 61:  # "+"
                self.get_game_visualizer().increase_current_tick_size(self.scaling_step)
                self.scene_gui_manager.show_message(
                    f"- size_tick_scale: {self.get_game_visualizer().get_current_tick_size()}"
                )

    def draw_grid(self):
        Grid.draw_grid(self.game_visualizer.get_screen(), self.game_visualizer.get_camera(),
                       self.game_visualizer.get_current_tick_size(), 1)
        draw_mouse_game_coordinates(self.game_visualizer.get_screen(), self.game_visualizer.get_camera(),
                                    self.game_visualizer.get_current_tick_size())
