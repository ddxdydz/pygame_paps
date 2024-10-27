import pygame

from basic.general_game_logic.base_objects.GameObject import GameObject


class CameraObject(GameObject):
    def __init__(self, coordinates, move_step):
        super().__init__(coordinates)
        self.move_step = move_step

    def set_move_step(self, move_step):
        self.move_step = move_step

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
