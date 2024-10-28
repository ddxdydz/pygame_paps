import pygame

from basic.audio.AudioManagerGUI import AudioManagerGUI
from basic.tools.loading_files import join_path


class AudioManager(AudioManagerGUI):
    def __init__(self):
        super().__init__()
        self.loaded_audio = dict()

        self.music_volume = 0.5
        self.volume_step = 0.05
        self.pause = False

    def load_audio_data(self, audio_library: dict):
        for audio_name in audio_library.keys():
            self.loaded_audio[audio_name] = join_path(audio_library[audio_name])

    def is_loaded_name(self, name):
        if name in self.loaded_audio.keys():
            return True
        print(f"AudioManager Error: Audio '{name}' is not founded.")
        return False

    def load_music(self, music_name):
        if self.is_loaded_name(music_name) and not self.pause:
            pygame.mixer.music.load(self.loaded_audio[music_name])
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(-1)

    def load_sound(self, sound_name):
        if self.is_loaded_name(sound_name):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.loaded_audio[sound_name]))

    def to_pause(self):
        self.pause = not self.pause
        if self.pause:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def decrease_volume(self):
        if self.pause:
            return
        self.music_volume -= self.volume_step
        if self.music_volume < 0:
            self.music_volume = 0
        pygame.mixer.music.set_volume(self.music_volume)

    def increase_volume(self):
        if self.pause:
            return
        self.music_volume += self.volume_step
        if self.music_volume > 1:
            self.music_volume = 1
        pygame.mixer.music.set_volume(self.music_volume)

    def process_event(self, event):
        if self.loaded_audio.keys():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.restart_showing_time()
                    self.to_pause()
                elif event.key == pygame.K_LEFT:
                    self.restart_showing_time()
                    self.decrease_volume()
                elif event.key == pygame.K_RIGHT:
                    self.restart_showing_time()
                    self.increase_volume()

    def draw_ui(self, screen):
        self.draw(screen, self.music_volume, self.pause)

    def update(self, fps):
        self.update_ui(fps)
