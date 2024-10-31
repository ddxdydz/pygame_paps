class CollisionRectChecker:
    @staticmethod
    def check_collision_1to2(rect1: tuple[tuple[float, float], ...],
                             rect2: tuple[tuple[float, float], ...]) -> bool:
        min_x1, max_y1 = rect1[0]
        max_x1, min_y1 = rect1[2]
        for x2, y2 in rect2:
            if min_x1 < x2 < max_x1:
                if min_y1 < y2 < max_y1:
                    return True
        return False

    @staticmethod
    def check_collision(rect1: tuple[tuple[float, float], ...],
                        rect2: tuple[tuple[float, float], ...]) -> bool:
        if (CollisionRectChecker.check_collision_1to2(rect1, rect2) or
                CollisionRectChecker.check_collision_1to2(rect2, rect1)):
            return True
        return False
