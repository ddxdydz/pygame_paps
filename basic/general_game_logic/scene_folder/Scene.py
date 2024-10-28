from basic.audio.AudioManager import AudioManager
from basic.general_game_logic.game_visualization.game_gui_visualization.GameGuiManager import GameGuiManager
from basic.general_game_logic.game_visualization.game_process_visualization.GameGraphicManager import GameGraphicManager
from basic.general_visualization.general_gui.Messanger import Messanger


class Scene:
    rules = "No rules"

    def __init__(self, screen, audio_manager: AudioManager = AudioManager()):
        self.audio_manager = audio_manager
        self.game_graphic_manager = GameGraphicManager(screen)
        self.game_gui_manager = GameGuiManager()

        self.messanger = Messanger()
        self.messanger.main_text_font_size_coefficient = 1 / 15
        self.messanger.annotation_text = "Для продолжения нажмите Enter..."
        self.messanger.end_key_code = 13  # enter

        self.is_over = False

        self.player_enable_updating = True

    def get_rules(self):
        return self.rules

    def get_screen(self):
        return self.game_graphic_manager.get_screen()

    def auto_size(self):
        self.get_game_graphic_manager().auto_set_tick_size(
            self.get_screen().get_size()
        )

    def get_audio_manager(self):
        return self.audio_manager

    def get_game_gui_manager(self):
        return self.game_gui_manager

    def get_game_graphic_manager(self):
        return self.game_graphic_manager

    def update_size_tick_scale(self, size_tick_scale):
        pass

    def process_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass
