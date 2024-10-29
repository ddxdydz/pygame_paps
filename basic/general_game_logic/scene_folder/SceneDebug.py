import pygame

from basic.audio.AudioManager import AudioManager
from basic.general_game_logic.scene_folder.Scene import Scene


class SceneDebug(Scene):
    def __init__(self, screen, audio_manager: AudioManager()):
        super().__init__(screen, audio_manager)
        self.show_debug_info = False

    def process_debug_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:  # free camera mod
                self.scene_gui_manager.switch_show_gui()
                self.game_visualizer.camera.switch_free_observing_mod()
                if self.game_visualizer.camera.is_free:
                    self.player_enable_updating = False
                else:
                    self.player_enable_updating = True
            elif event.key == pygame.K_v:
                self.scene_gui_manager.switch_show_gui()
            elif event.key == pygame.K_p:
                self.show_debug_info = not self.show_debug_info
            elif event.key == pygame.K_m:
                width, height = self.game_visualizer.get_screen().get_size()
                cur_scale = self.get_game_visualizer().get_current_tick_size()
                self.scene_gui_manager.show_message(
                    f"- screen size: {width}x{height}, size_tick_scale: {cur_scale}"
                )
            elif event.key == 45:  # "-"
                self.get_game_visualizer().decrease_current_tick_size(5)
                self.scene_gui_manager.show_message(
                    f"size_tick_scale: {self.get_game_visualizer().get_current_tick_size()}"
                )
            elif event.key == 61:  # "+"
                self.get_game_visualizer().increase_current_tick_size(5)
                self.scene_gui_manager.show_message(
                    f"size_tick_scale: {self.get_game_visualizer().get_current_tick_size()}"
                )
