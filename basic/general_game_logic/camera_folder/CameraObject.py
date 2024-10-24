import pygame

from basic.general_settings import FPS, WINDOW_SIZE
from basic.general_game_logic.game_base_settings import ONE_TICK_TO_PX, CAMERA_SPEED
from basic.general_game_logic.base_objects.GameObject import GameObject

WINDOWS_PER_SECOND = CAMERA_SPEED


class CameraObject(GameObject):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        ticks_count = min(WINDOW_SIZE) / ONE_TICK_TO_PX
        self.move_step = (ticks_count * WINDOWS_PER_SECOND) / FPS

    def get_move_step(self):
        return self.move_step

    def keys_update(self, keys):
        if keys[pygame.K_w]:
            self.add_to_coordinates(0, self.move_step)
        if keys[pygame.K_s]:
            self.add_to_coordinates(0, -self.move_step)
        if keys[pygame.K_a]:
            self.add_to_coordinates(-self.move_step, 0)
        if keys[pygame.K_d]:
            self.add_to_coordinates(self.move_step, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        self.keys_update(keys)
