import sys

import pygame

from basic.audio.AudioManager import AudioManager
from basic.general_settings import FPS
from basic.tools.get_center_drawing_coordinates import get_center_drawing_coordinates


class Messanger:
    def __init__(self, audio_manager=AudioManager()):
        self.audio_manager = audio_manager
        self.end_key_code = None

        self.background_screen_color = pygame.Color(20, 20, 20, 200)

        self.main_text_color = (235, 235, 235, 255)
        self.main_text_font_size_coefficient = 1 / 22
        self.showing_main_text = ""

        self.annotation_color = (200, 200, 200, 180)
        self.annotation_font_size_proportions = 0.6  # annotation_size = text_size * 0.5
        self.annotation_text = "Для продолжения нажмите любую кнопку..."

    def get_main_text_size(self, screen: pygame.Surface) -> int:
        return int(screen.get_height() * self.main_text_font_size_coefficient)

    def get_annotation_text_size(self, screen: pygame.Surface) -> int:
        return int(self.get_main_text_size(screen) * self.annotation_font_size_proportions)

    def get_main_text(self, screen: pygame.Surface) -> pygame.Surface:
        message_font = pygame.font.Font(None, self.get_main_text_size(screen))
        text = message_font.render(self.showing_main_text, True, self.main_text_color)
        return text

    def get_annotation_text(self, screen: pygame.Surface) -> pygame.Surface:
        annotation_font = pygame.font.Font(None, self.get_annotation_text_size(screen))
        text = annotation_font.render(self.annotation_text, True, self.annotation_color)
        return text

    def get_message_background(self, screen: pygame.Surface) -> pygame.Surface:
        background = pygame.Surface(screen.get_size()).convert_alpha()
        background.fill(self.background_screen_color)
        return background

    def draw_message(self, screen: pygame.Surface):
        main_text = self.get_main_text(screen)
        annotation_text = self.get_annotation_text(screen)

        main_text_x, main_text_y = get_center_drawing_coordinates(screen, main_text)
        annotation_text_x, _ = get_center_drawing_coordinates(screen, annotation_text)
        annotation_text_y = main_text_y + main_text.get_height() + 2 * annotation_text.get_height()

        screen.blit(self.get_message_background(screen), (0, 0))
        screen.blit(main_text, (main_text_x, main_text_y))
        screen.blit(annotation_text, (annotation_text_x, annotation_text_y))

    def enable_messanger_loop(self, screen: pygame.Surface):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get().copy():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    if self.end_key_code is None:
                        return event
                    elif event.type == pygame.KEYDOWN:
                        if event.key == self.end_key_code:
                            running = False

            self.draw_message(screen)

            if self.audio_manager is not None:
                self.audio_manager.update(FPS)
                self.audio_manager.draw_ui(screen)

            clock.tick(FPS)
            pygame.display.flip()

    def show_message(self, screen, message):
        self.showing_main_text = message
        return self.enable_messanger_loop(screen)
