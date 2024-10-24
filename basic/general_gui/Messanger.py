import sys
import pygame

from basic.general_settings import FPS


class Messanger:
    def __init__(self, audio_manager=None):
        self.audio_manager = audio_manager
        self.end_key_code = None
        self.background_screen_color = pygame.Color(20, 20, 20, 200)
        self.message_color = (235, 235, 235, 255)
        self.message_font_size = 60
        self.annotation_color = (200, 200, 200, 180)
        self.annotation_font_size = 25
        self.annotation_text = "Для продолжения нажмите любую кнопку..."

    def draw_annotation(self, screen_for_draw):
        annotation_font = pygame.font.Font(None, self.annotation_font_size)
        text = annotation_font.render(
            self.annotation_text, True, self.annotation_color)
        width, height = text.get_size()
        x = (screen_for_draw.get_width() - width) // 2
        y = (screen_for_draw.get_height() - height - 80)
        screen_for_draw.blit(text, (x, y))

    def draw_message(self, message, screen_for_draw):
        message_screen = pygame.Surface(screen_for_draw.get_size()).convert_alpha()
        message_screen.fill(self.background_screen_color)
        screen_for_draw.blit(message_screen, (0, 0))

        # Вывод сообщения:
        message_font = pygame.font.Font(None, self.message_font_size)
        text = message_font.render(message, True, self.message_color)
        width, height = text.get_size()
        x = (screen_for_draw.get_width() - width) // 2
        y = (screen_for_draw.get_height() - height) // 2
        screen_for_draw.blit(text, (x, y))

        # Вывод пояснения:
        self.draw_annotation(screen_for_draw)

    def enable_messanger_loop(self, screen):
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

            if self.audio_manager is not None:
                self.audio_manager.update(FPS)
                self.audio_manager.draw_ui(screen)

            clock.tick(FPS)
            pygame.display.flip()

    def show_message(self, message, screen_for_draw):
        self.draw_message(message, screen_for_draw)
        return self.enable_messanger_loop(screen_for_draw)
