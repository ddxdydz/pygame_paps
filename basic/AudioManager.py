import pygame

from basic.loading_files import join_path, load_image
from basic.local_constants import AUDIO_PATHS, IMAGE_PATHS, FPS


class AudioManager:
    sound_off_img = load_image(IMAGE_PATHS["audio_off"], size=(50, 50))
    sound_on_img = load_image(IMAGE_PATHS["audio_on"], size=(50, 50))

    def __init__(self):
        self.music_volume = 0.5
        self.pause = False
        self.volume_step = 0.05

        self.fps = FPS
        self.time_for_showing = 2  # sec
        self.current_time = 0

    def load_menu_music(self):
        pygame.mixer.music.load(join_path(AUDIO_PATHS["menu"]))
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def load_game_music(self):
        pygame.mixer.music.load(join_path(AUDIO_PATHS["game"]))
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def load_lose_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(join_path(AUDIO_PATHS["lose"])))

    def load_coin_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(join_path(AUDIO_PATHS["coin"])))

    def load_win_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(join_path(AUDIO_PATHS["win"])))

    def load_notification_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(join_path(AUDIO_PATHS["notification"])))

    def load_achievement_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(join_path(AUDIO_PATHS["achievement"])))

    def to_pause(self):
        self.pause = not self.pause
        if self.pause:
            pygame.mixer.music.pause()
            # print("pause")
        else:
            pygame.mixer.music.unpause()
            # print("unpause")

    def decrease_volume(self):
        self.music_volume -= self.volume_step
        if self.music_volume < 0:
            self.music_volume = 0
        pygame.mixer.music.set_volume(self.music_volume)
        # print(pygame.mixer.music.get_volume())

    def increase_volume(self):
        self.music_volume += self.volume_step
        if self.music_volume > 1:
            self.music_volume = 1
        pygame.mixer.music.set_volume(self.music_volume)
        # print(pygame.mixer.music.get_volume())

    def process_event(self, event):
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
        self.fps = fps
        delta = self.time_for_showing / self.fps
        self.current_time -= delta
        if self.current_time < 0:
            self.current_time = 0

    def draw_ui(self, screen):
        if self.current_time == 0:
            return

        size = width, height = 50, 65  # px
        left_padding = (screen.get_size()[0] - width) // 2
        upper_padding = 20

        audio_state_surface = pygame.Surface(size).convert_alpha()
        audio_state_surface.fill("black")

        if self.pause:
            audio_state_surface.blit(AudioManager.sound_off_img, (2, 0))
        else:
            audio_state_surface.blit(AudioManager.sound_on_img, (2, 0))

        annotation_font = pygame.font.Font(None, 20)
        text = annotation_font.render(f"   {round(pygame.mixer.music.get_volume() * 100)}%", True, "white")
        audio_state_surface.blit(text, (0, AudioManager.sound_on_img.height))

        audio_state_surface.set_alpha(int(255 * (self.current_time / self.time_for_showing)))
        screen.blit(audio_state_surface, (left_padding, upper_padding))
