from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.camera_folder.CameraObject import CameraObject
from basic.general_settings import CAMERA_SPEED, FPS
from basic.general_settings import ONE_TICK_TO_PX, WINDOW_SIZE


WINDOWS_PER_SECOND = CAMERA_SPEED


class Camera(GameObject):
    def __init__(self, coordinates=(0, 0), screen_size=WINDOW_SIZE, size_tick_scale=ONE_TICK_TO_PX):
        super().__init__(coordinates)

        # Default object
        self.camera_object = CameraObject((0, 0), 0)

        # Set visualization parameters
        self.update_visualization_parameters(screen_size, size_tick_scale)

        # Observed parameters:
        self.observed_object = self.camera_object

        # Mods parameters:
        self.is_free = True

    # Camera actions:

    def fix_camera_on_object(self, obj: GameObject):
        self.is_free = False
        self.observed_object = obj

    def fix_camera_on_coordinates(self, coordinates):
        self.is_free = False
        self.camera_object.set_coordinates(coordinates)
        self.observed_object = self.camera_object

    def enable_free_observing_mod(self):
        self.is_free = True
        self.camera_object.set_coordinates(self.observed_object.get_centre_coordinates())
        self.observed_object = self.camera_object

    # Info

    def get_info(self):
        return f"""
                    CAMERA:
            Coordinates: {self.get_coordinates()}
            Coordinates centre: {self.get_centre_coordinates()}
            Coordinates camera_object {self.camera_object.get_coordinates()}
            Coordinates observed_object {self.observed_object.get_coordinates()}
            Coordinates center observed_object {self.observed_object.get_centre_coordinates()}

        """

    # For updating:
    def update_visualization_parameters(self, screen_size, size_tick_scale):
        self.set_obj_size((screen_size[0] / size_tick_scale, screen_size[1] / size_tick_scale))
        ticks_count = min(screen_size) / size_tick_scale
        self.camera_object.set_move_step((ticks_count * WINDOWS_PER_SECOND) / FPS)

    def update_coordinates(self):
        xc, yc = self.observed_object.get_centre_coordinates()
        self.set_coordinates((xc - self.width / 2, yc + self.height / 2))

    def update(self):
        self.update_coordinates()
        if self.is_free:
            self.camera_object.update()
