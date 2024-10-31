class CollisionRect:
    def __init__(self, img_x, img_y, width,  height):
        self.collision_rect = tuple()  # ticks_x, ticks_y in image left upper corner + weight, height
        self.collision_rect_points = tuple()  # same, but in 4 points
        self.set_collision_rect(img_x, img_y, width,  height)

    def set_collision_rect(self, x, y, width, height):
        self.collision_rect = (x, y, width, height)
        self.collision_rect_points = (
            (x, y),
            (x + width, y),
            (x + width, y - height),
            (x, y - height)
        )

    def get_rect(self) -> tuple[tuple[float, float], ...]:
        return self.collision_rect

    def get_points(self) -> tuple[tuple[float, float], ...]:
        return self.collision_rect_points

    def get_rect_size(self):
        return self.collision_rect[2], self.collision_rect[3]

    def get_absolute_coordinates(self, main_x, main_y) -> tuple[tuple[float, float], ...]:
        rect_coordinates = []
        for point_x, point_y in self.get_points():
            rect_coordinates.append((main_x + point_x, main_y + point_y))
        return tuple(rect_coordinates)
