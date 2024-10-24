from basic.general_game_logic.camera_folder.Camera import Camera
from basic.general_game_logic.visualization.GamingDisplayManager import GamingDisplayManager
from basic.general_game_logic.visualization.GamingGuiManager import GamingGuiManager
from basic.general_gui.Messanger import Messanger


class Scene:
    def __init__(self, screen, audio_manager):
        self.screen = screen
        self.audio_manager = audio_manager
        self.messanger = Messanger()
        self.messanger.annotation_text = "Для продолжения нажмите на Enter..."
        self.messanger.end_key_code = 13  # enter
        self.camera = Camera()
        self.display_manager = GamingDisplayManager(self.camera, screen)
        self.gaming_gui_manager = GamingGuiManager()

    def get_screen(self):
        return self.screen

    def process_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass
