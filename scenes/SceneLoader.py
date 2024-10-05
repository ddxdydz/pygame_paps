import sys
import pygame

from scenes.scene1.Scene1 import Scene1
from basic.Messanger import Messanger
from basic.local_constants import FPS


class SceneLoader:
    def __init__(self, audio_manager):
        self.audio_manager = audio_manager
        self.messanger = Messanger(self.audio_manager)

    def load(self, screen):
        scene = Scene1(screen, self.audio_manager)

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
                        self.audio_manager.load_notification_sound()
                        mes_event = self.messanger.show_message(
                            "Для выхода в главное меню нажмите Enter", screen)
                        if mes_event.type == pygame.KEYDOWN:
                            if mes_event.key == 13:  # enter
                                self.audio_manager.load_lose_sound()
                                running = False
                self.audio_manager.process_event(event)
                scene.process_event(event)

            if scene.is_over:
                running = False
            else:
                scene.update()
                screen.fill("black")
                scene.draw(screen)

            self.audio_manager.update(FPS)
            self.audio_manager.draw_ui(screen)

            pygame.display.flip()
            clock.tick(FPS)
