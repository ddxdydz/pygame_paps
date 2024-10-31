from basic.audio.AudioManager import AudioManager
from basic.basic_gui.FullScreenMessanger import FullScreenMessanger
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from basic.general_game_logic.scene_folder.GuiManagerScene import GuiManagerScene


class Scene:
    rules = "No rules"

    def __init__(self, screen, audio_manager: AudioManager = AudioManager()):
        self.audio_manager = audio_manager
        self.game_visualizer = GameVisualizer(screen)
        self.scene_gui_manager = GuiManagerScene(screen)

        self.messanger = FullScreenMessanger()
        self.messanger.main_text_font_size_coefficient = 1 / 15
        self.messanger.annotation_text = "Для продолжения нажмите Enter..."
        self.messanger.end_key_code = 13  # enter

        self.is_over = False

    def get_rules(self):
        return self.rules

    def get_screen(self):
        return self.game_visualizer.get_screen()

    def auto_size(self):
        self.get_game_visualizer().auto_set_tick_size(
            self.get_screen().get_size()
        )

    def get_audio_manager(self):
        return self.audio_manager

    def set_scene_gui_manager(self, scene_gui_manager: GuiManagerScene):
        self.scene_gui_manager = scene_gui_manager

    def get_scene_gui_manager(self):
        return self.scene_gui_manager

    def get_game_visualizer(self):
        return self.game_visualizer

    def update_size_tick_scale(self, size_tick_scale):
        pass

    def process_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass
