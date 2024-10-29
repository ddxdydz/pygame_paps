import pygame

from basic.tools.screen_placement.get_drawing_center_coordinates import get_drawing_center_coordinates
from basic.tools.get_dynamic_alpha import get_dynamic_alpha


class AudioManagerGUI:
    def __init__(self):
        self.time_showing = 5  # sec
        self.time_start_decrease_alpha = 2
        self.current_time = 0
        self.default_visibility = 255
        self.size = self.width, self.height = 100, 100  # px

    def restart_showing_time(self):
        self.current_time = self.time_showing

    def get_audio_state_surface(self):
        audio_state_surface = pygame.Surface(self.size).convert_alpha()
        audio_state_surface.fill("blue")
        audio_state_surface.set_colorkey("blue")
        pygame.draw.rect(audio_state_surface, "black", (0, 0, *self.size), border_radius=self.width // 4)
        return audio_state_surface

    def get_text_surface(self, volume, is_pause):
        text_size = self.width // 4
        text = f" music\n    is\npaused"
        if not is_pause:
            text = f" music\nvolume\n   {round(volume * 100)}%"
        font = pygame.font.Font(None, text_size)
        return font.render(text, True, "white")

    def update_ui(self, fps):
        self.current_time -= self.time_showing / fps
        if self.current_time < 0:
            self.current_time = 0

    def draw(self, screen, volume, is_pause):
        if self.current_time == 0:
            return

        text_surface = self.get_text_surface(volume, is_pause)
        audio_state_surface = self.get_audio_state_surface()
        audio_state_surface.blit(
            text_surface, get_drawing_center_coordinates(
                audio_state_surface, text_surface)
        )

        audio_state_surface.set_alpha(get_dynamic_alpha(
            self.time_showing, self.time_start_decrease_alpha,
            self.current_time, self.default_visibility
        ))

        left_padding = (screen.width - self.width) // 2
        upper_padding = round(screen.height * 0.02)
        screen.blit(audio_state_surface, (left_padding, upper_padding))
