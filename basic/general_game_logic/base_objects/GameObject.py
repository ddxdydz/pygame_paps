from math import hypot, inf


class GameObject:
    def __init__(self, coordinates: tuple, size: (int, int) = (0, 0)):
        self.x0, self.y0 = coordinates  # left upper corner in main cords
        self.size = self.width, self.height = size
        self.deleted = False

    def is_deleted(self):
        return self.deleted

    def delete(self):
        self.deleted = True

    def set_size(self, size):
        self.size = self.width, self.height = size

    def get_size(self):
        return self.size

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]

    def get_coordinates(self):
        return self.x0, self.y0

    def get_x(self):
        return self.x0

    def get_y(self):
        return self.y0

    def set_coordinates(self, new_coordinates: tuple):
        self.x0, self.y0 = new_coordinates

    def add_to_coordinates(self, delta_x, delta_y):
        self.x0 += delta_x
        self.y0 += delta_y

    def get_centre_coordinates(self):
        return self.x0 + self.width / 2, self.y0 - self.height / 2

    def get_distance_between_centres(self, obj) -> float:
        if isinstance(obj, GameObject):
            self_cx, self_cy = self.get_centre_coordinates()
            obj_cx, obj_cy = obj.get_centre_coordinates()
            return hypot(abs(self_cx - obj_cx), abs(self_cy - obj_cy))
        return inf

    def get_no_contact_distance(self, obj) -> float:
        if isinstance(obj, GameObject):
            return (hypot(*self.size) + hypot(*obj.get_size())) * 0.6
        return inf

    def update(self, *args, **kwargs):
        pass
