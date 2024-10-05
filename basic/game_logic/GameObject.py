class GameObject:
    def __init__(self, coordinates: tuple, size: (int, int) = (0, 0)):
        self.x0, self.y0 = coordinates  # left upper corner in main cords
        self.size = self.width, self.height = size
        self.deleted = False

    def is_deleted(self):
        return self.deleted

    def delete(self):
        self.deleted = True

    def get_coordinates(self):
        return self.x0, self.y0

    def set_coordinates(self, new_coordinates: tuple):
        self.x0, self.y0 = new_coordinates

    def get_centre_coordinates(self):
        return self.x0 + self.width / 2, self.y0 - self.height / 2

    def move(self, x_step, y_step):
        self.x0 += x_step
        self.y0 += y_step

    def update(self, *args, **kwargs):
        pass
