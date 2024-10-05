import pygame

from basic.game_logic.GameObject import GameObject
from basic.local_constants import FPS, WINDOW_SIZE
from basic.game_logic.game_constants import ONE_TICK_TO_PX


WINDOWS_PER_SECOND = 2


class CameraObject(GameObject):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        ticks_count = min(WINDOW_SIZE) / ONE_TICK_TO_PX
        self.move_step = (ticks_count * WINDOWS_PER_SECOND) / FPS

    def get_move_step(self):
        return self.move_step

    def keys_update(self, keys):
        if keys[pygame.K_w]:
            self.move(0, self.move_step)
        if keys[pygame.K_s]:
            self.move(0, -self.move_step)
        if keys[pygame.K_a]:
            self.move(-self.move_step, 0)
        if keys[pygame.K_d]:
            self.move(self.move_step, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        self.keys_update(keys)
