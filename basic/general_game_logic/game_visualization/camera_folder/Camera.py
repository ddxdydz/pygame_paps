from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.game_visualization.camera_folder.CameraObject import CameraObject
from basic.general_settings import CAMERA_SPEED, FPS


class Camera(GameObject):
    def __init__(self, coordinates=(0, 0)):
        super().__init__(coordinates)

        # Default object
        self.camera_object = CameraObject((0, 0), 0)

        # Observed parameters:
        self.basic_observed_object = self.camera_object
        self.current_observed_object = self.camera_object

        # Mods parameters:
        self.is_free = True

    # Camera actions:

    def fix_camera_on_object(self, obj: GameObject):
        self.is_free = False
        self.basic_observed_object = obj
        self.current_observed_object = obj

    def fix_camera_on_coordinates(self, coordinates):
        self.is_free = False
        self.basic_observed_object = GameObject(coordinates)
        self.current_observed_object = self.basic_observed_object

    def enable_free_observing_mod(self):
        self.is_free = True
        self.camera_object.set_coordinates(
            self.basic_observed_object.get_centre_coordinates()
        )
        self.current_observed_object = self.camera_object

    def disable_free_observing_mod(self):
        self.is_free = False
        self.current_observed_object = self.basic_observed_object

    def switch_free_observing_mod(self):
        if self.is_free:
            self.disable_free_observing_mod()
        else:
            self.enable_free_observing_mod()

    # Info

    def get_info(self):
        return f"""
                    CAMERA:
            Coordinates: {self.get_coordinates()}
            Coordinates centre: {self.get_centre_coordinates()}
            Coordinates camera_object {self.camera_object.get_coordinates()}
            Coordinates current_observed_object {self.current_observed_object.get_coordinates()}
            Coordinates center current_observed_object {self.current_observed_object.get_centre_coordinates()}

        """

    # For updating

    def update_camera_size(self, screen_size, size_tick_scale):
        self.set_size((screen_size[0] / size_tick_scale, screen_size[1] / size_tick_scale))

    def update_camera_speed(self, screen_size, size_tick_scale):
        ticks_count = min(screen_size) / size_tick_scale
        self.camera_object.set_move_step((ticks_count * CAMERA_SPEED) / FPS)

    def update_coordinates(self):
        xc, yc = self.current_observed_object.get_centre_coordinates()
        self.set_coordinates((xc - self.width / 2, yc + self.height / 2))

    def update(self, screen_size, size_tick_scale):
        self.update_camera_size(screen_size, size_tick_scale)
        self.update_camera_speed(screen_size, size_tick_scale)
        self.update_coordinates()
        if self.is_free:
            self.camera_object.update()
