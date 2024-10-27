from basic.audio.AudioManager import AudioManager
from basic.general_game_logic.camera_folder.Camera import Camera
from basic.general_game_logic.visualization.GameDisplayManager import GameDisplayManager
from basic.general_game_logic.visualization.GameGuiManager import GameGuiManager
from basic.general_visualization.general_gui.Messanger import Messanger


class Scene:
    def __init__(self, screen, audio_manager: AudioManager()):
        self.audio_manager = audio_manager

        self.messanger = Messanger()
        self.messanger.main_text_font_size_coefficient = 1 / 15
        self.messanger.annotation_text = "Для продолжения нажмите Enter..."
        self.messanger.end_key_code = 13  # enter

        self.display_manager = GameDisplayManager(screen)
        self.game_gui_manager = GameGuiManager()

        self.rules = "No rules"
        self.is_over = False

    def get_rules(self):
        return self.rules

    def get_screen(self):
        return self.display_manager.get_screen()

    def get_audio_manager(self):
        return self.audio_manager

    def get_game_gui_manager(self):
        return self.game_gui_manager

    def get_display_manager(self):
        return self.display_manager

    def update_size_tick_scale(self, size_tick_scale):
        pass

    def process_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass
