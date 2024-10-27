import pygame

from basic.tools.loading_files import join_path, load_image
from basic.general_settings import IMAGE_PATHS, FPS


class AudioManager:
    def __init__(self, enable=True):
        self.loaded_audio = dict()
        self.loaded_images = dict()
        if enable:
            self.load_images()

        self.enable = enable

        self.music_volume = 0.5
        self.pause = False
        self.volume_step = 0.05

        self.fps = FPS
        self.time_for_showing = 2  # sec
        self.current_time = 0

    def load_audio_data(self, audio_library: dict):
        for audio_name in audio_library.keys():
            self.loaded_audio[audio_name] = join_path(audio_library[audio_name])

    def is_loaded_name(self, name):
        if name in self.loaded_audio.keys():
            return True
        print(f"Аудио '{name}' не найдено.")
        return False

    def load_images(self):
        self.loaded_images["audio_off"] = load_image(IMAGE_PATHS["audio_off"], size=(50, 50))
        self.loaded_images["audio_on"] = load_image(IMAGE_PATHS["audio_on"], size=(50, 50))

    def load_music(self, music_name):
        if self.enable and self.is_loaded_name(music_name) and not self.pause:
            pygame.mixer.music.load(self.loaded_audio[music_name])
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(-1)

    def load_sound(self, sound_name):
        if self.enable and self.is_loaded_name(sound_name):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.loaded_audio[sound_name]))

    def to_pause(self):
        if not self.enable:
            return
        self.pause = not self.pause
        if self.pause:
            pygame.mixer.music.pause()
            # print("pause")
        else:
            pygame.mixer.music.unpause()
            # print("unpause")

    def decrease_volume(self):
        if not self.enable:
            return
        self.music_volume -= self.volume_step
        if self.music_volume < 0:
            self.music_volume = 0
        pygame.mixer.music.set_volume(self.music_volume)
        # print(pygame.mixer.music.get_volume())

    def increase_volume(self):
        if not self.enable:
            return
        self.music_volume += self.volume_step
        if self.music_volume > 1:
            self.music_volume = 1
        pygame.mixer.music.set_volume(self.music_volume)
        # print(pygame.mixer.music.get_volume())

    def process_event(self, event):
        if not self.enable:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.current_time = self.time_for_showing
                self.to_pause()
            elif event.key == pygame.K_LEFT:
                self.current_time = self.time_for_showing
                self.decrease_volume()
            elif event.key == pygame.K_RIGHT:
                self.current_time = self.time_for_showing
                self.increase_volume()

    def update(self, fps):
        if not self.enable:
            return
        self.fps = fps
        delta = self.time_for_showing / self.fps
        self.current_time -= delta
        if self.current_time < 0:
            self.current_time = 0

    def draw_ui(self, screen):
        if not self.enable:
            return
        if self.current_time == 0:
            return

        size = width, height = 100, 100  # px

        text_size = width // 5
        audio_state_surface = pygame.Surface(size).convert_alpha()
        audio_state_surface.fill("blue")
        audio_state_surface.set_colorkey("blue")
        pygame.draw.rect(audio_state_surface, "black", (0, 0, *size), border_radius=width // 4)

        img_width, img_height = self.loaded_images["audio_off"].size

        surface_upper_padding = (height - img_height - text_size) // 2

        if self.pause:
            audio_state_surface.blit(self.loaded_images["audio_off"], ((width - img_width) // 2, surface_upper_padding))
        else:
            audio_state_surface.blit(self.loaded_images["audio_on"], ((width - img_width) // 2, surface_upper_padding))

        annotation_font = pygame.font.Font(None, text_size)
        text = annotation_font.render(f"{round(pygame.mixer.music.get_volume() * 100)}%", True, "white")
        audio_state_surface.blit(text, ((width - text.width) // 2, surface_upper_padding + img_height))

        audio_state_surface.set_alpha(int(255 * (self.current_time / self.time_for_showing)))
        left_padding = (screen.width - width) // 2
        upper_padding = round(screen.height * 0.02)
        screen.blit(audio_state_surface, (left_padding, upper_padding))
