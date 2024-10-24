import sys
import pygame

from basic.general_gui.Messanger import Messanger
from basic.general_settings import FPS


class SceneLoader:
    def __init__(self, audio_manager):
        self.audio_manager = audio_manager
        self.messanger = Messanger(self.audio_manager)

    def load(self, scene):
        clock = pygame.time.Clock()

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
                            "Для выхода в главное меню нажмите Enter", scene.get_screen())
                        if mes_event.type == pygame.KEYDOWN:
                            if mes_event.key == 13:  # enter
                                self.audio_manager.load_sound("lose")
                                running = False
                self.audio_manager.process_event(event)
                scene.process_event(event)

            if scene.is_over:
                running = False
            else:
                scene.update()
                scene.get_screen().fill("black")
                scene.draw(scene.get_screen())

            self.audio_manager.update(FPS)
            self.audio_manager.draw_ui(scene.get_screen())

            pygame.display.flip()
            clock.tick(FPS)
