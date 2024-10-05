import pygame

from basic.game_logic.GameObject import GameObject
from basic.game_logic.camera_folder.CameraObject import CameraObject
from basic.game_logic.game_constants import ONE_TICK_TO_PX
from basic.local_constants import WINDOW_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT


class Camera(GameObject):

    def __init__(self, coordinates=(0, 0)):
        super().__init__(coordinates, size=(
            WINDOW_WIDTH / ONE_TICK_TO_PX, WINDOW_HEIGHT / ONE_TICK_TO_PX
        ))

        # Default object
        self.camera_object = CameraObject((0, 0))

        # Observed parameters:
        self.observed_object = self.camera_object

        # Mods parameters:
        self.is_free = True
        self.grid_mod = False

    # Fixed camera functions:

    def fix_camera_on_object(self, obj: GameObject):
        self.is_free = False
        self.observed_object = obj

    def fix_camera_on_coordinates(self, coordinates):
        self.is_free = False
        self.camera_object.set_coordinates(coordinates)
        self.observed_object = self.camera_object

    # Free observing mod functions:

    def enable_free_observing_mod(self):
        self.camera_object.set_coordinates(
            self.observed_object.get_centre_coordinates())
        self.observed_object = self.camera_object
        self.is_free = True

    def update_free_observing_mod(self):
        if self.is_free:
            self.camera_object.update()

    # Info

    def get_info(self):
        return f"""
                    CAMERA:
            Coordinates: {self.get_coordinates()}
            Coordinates centre: {self.get_centre_coordinates()}
            Coordinates camera_object {self.camera_object.get_coordinates()}
            Coordinates observed_object {self.observed_object.get_coordinates()}
            Coordinates center observed_object {self.observed_object.get_centre_coordinates()}
            self.grid_mod: {self.grid_mod}

        """

    # For updating:

    def update_coordinates(self):
        xc, yc = self.observed_object.get_centre_coordinates()
        self.set_coordinates((xc - self.width / 2, yc + self.height / 2))

    def update(self):
        self.update_coordinates()
        self.update_free_observing_mod()
