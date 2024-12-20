import sys

import pygame

from basic.audio.AudioManager import AudioManager
from basic.general_settings import FPS, IMAGE_PATHS
from basic.tools.screen_placement.get_drawing_center_coordinates import get_drawing_center_coordinates
from basic.tools.loading.loading_files import load_image


class FullScreenMessanger:
    def __init__(self, audio_manager=AudioManager()):
        self.audio_manager = audio_manager
        self.end_key_code = None

        self.background_screen_color = pygame.Color(20, 20, 20)
        self.default_visible = 200

        self.main_text_color = (235, 235, 235, 255)
        self.main_text_font_size_coefficient = 1 / 20
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

    def get_text_surface(self, screen: pygame.Surface) -> pygame.Surface:
        main_text = self.get_main_text(screen)
        annotation_text = self.get_annotation_text(screen)

        width = max(main_text.get_width(), annotation_text.get_width())
        height = main_text.get_height() + 2 * annotation_text.get_height()

        text_surface = pygame.Surface((width, height)).convert_alpha()
        text_surface.fill("black")
        text_surface.set_colorkey("black")

        main_text_x, _ = get_drawing_center_coordinates(text_surface, main_text)
        annotation_text_x, _ = get_drawing_center_coordinates(text_surface, annotation_text)
        annotation_text_y = main_text.get_height() + annotation_text.get_height()

        text_surface.blit(main_text, (main_text_x, 0))
        text_surface.blit(annotation_text, (annotation_text_x, annotation_text_y))
        return text_surface

    def get_message_background(self, screen: pygame.Surface) -> pygame.Surface:
        background = pygame.Surface(screen.get_size()).convert_alpha()
        background.fill(self.background_screen_color)
        background.set_alpha(self.default_visible)
        return background

    def draw_message(self, screen: pygame.Surface, default_background: pygame.Surface):
        text_surface = self.get_text_surface(screen)
        default_background.blit(self.get_message_background(screen), (0, 0))
        default_background.blit(text_surface, get_drawing_center_coordinates(default_background, text_surface))
        screen.blit(default_background)

    def enable_messanger_loop(self, screen: pygame.Surface):
        running = True
        clock = pygame.time.Clock()

        default_screen = pygame.Surface(screen.get_size())
        default_screen.blit(screen)

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
                elif event.type == pygame.KEYDOWN:
                    if event.key == 13:  # Enter
                        mods = pygame.key.get_mods()
                        if mods & pygame.KMOD_ALT:
                            pygame.display.toggle_fullscreen()
                            pygame.display.set_icon(load_image(IMAGE_PATHS["icon"]))

            default_background = pygame.Surface(screen.get_size())
            default_background.blit(default_screen)
            self.draw_message(screen, default_background)

            if self.audio_manager is not None:
                self.audio_manager.update(FPS)
                self.audio_manager.draw_ui(screen)

            clock.tick(FPS)
            pygame.display.flip()

    def show_message(self, screen, message):
        self.showing_main_text = message
        return self.enable_messanger_loop(screen)
