import sys

import pygame

from basic.audio.AudioManager import AudioManager
from basic.basic_gui.FullScreenMessanger import FullScreenMessanger
from basic.basic_gui.gui_elements.FpsBar import FpsBar
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import FPS, IMAGE_PATHS
from basic.tools.loading.loading_files import load_image


class SceneLoader:
    def __init__(self, audio_manager: AudioManager = AudioManager()):
        self.audio_manager = audio_manager
        self.messanger = FullScreenMessanger(self.audio_manager)
        self.fps_bar = FpsBar()

    def load(self, scene: Scene):
        scene.auto_size()

        clock = pygame.time.Clock()

        self.audio_manager.load_music("game")

        running = True
        while running:
            events = pygame.event.get().copy()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.audio_manager.load_sound("notification")
                        mes_event = self.messanger.show_message(
                            scene.get_screen(),
                            "Для выхода в главное меню нажмите Enter"
                        )
                        if mes_event.type == pygame.KEYDOWN:
                            if mes_event.key == 13:  # enter
                                running = False
                    elif event.key == pygame.K_TAB:
                        self.fps_bar.change_show()
                    elif event.key == 13:  # Enter
                        mods = pygame.key.get_mods()
                        if mods & pygame.KMOD_ALT:
                            pygame.display.toggle_fullscreen()
                            pygame.display.set_icon(load_image(IMAGE_PATHS["icon"]))
                if event.type == pygame.VIDEORESIZE:
                    scene.auto_size()

                self.audio_manager.process_event(event)
                scene.process_event(event)

            scene.update()
            scene.draw()
            if scene.is_over:
                running = False

            self.fps_bar.show_fps(scene.get_screen(), int(clock.get_fps()))

            self.audio_manager.update(FPS)
            self.audio_manager.draw_ui(scene.get_screen())

            pygame.display.flip()
            clock.tick(FPS)
