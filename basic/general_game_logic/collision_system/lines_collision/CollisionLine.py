class CollisionLine:
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float]):
        x1, y1 = point1
        x2, y2 = point2
        self.point1 = (x1, y1)
        self.point2 = (x2, y2)
        self.nap_vector = (x2 - x1, y2 - y1)
        self.y_border = (min(y1, y2), max(y1, y2))
        self.x_border = (min(x1, x2), max(x1, x2))
        self.max_y_point = max(((x1, y1), (x2, y2)), key=lambda c: c[1])
