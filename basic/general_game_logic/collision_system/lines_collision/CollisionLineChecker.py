from math import acos, sqrt, inf

from basic.general_game_logic.collision_system.lines_collision.CollisionLine import CollisionLine


class CollisionLineChecker:
    @staticmethod
    def get_degree(vector1: tuple[float, float], vector2: tuple[float, float]) -> float:
        m1, l1 = vector1
        m2, l2 = vector2
        abs1, abs2 = sqrt(m1 ** 2 + l1 ** 2), sqrt(m2 ** 2 + l2 ** 2)
        return acos(abs(m1 * m2 + l1 * l2) / (abs1 * abs2))

    @staticmethod
    def get_degree_without_abs(vector1: tuple[float, float], vector2: tuple[float, float]) -> float:
        m1, l1 = vector1
        m2, l2 = vector2
        abs1, abs2 = sqrt(m1 ** 2 + l1 ** 2), sqrt(m2 ** 2 + l2 ** 2)
        return acos((m1 * m2 + l1 * l2) / (abs1 * abs2))

    @staticmethod
    def get_crossing_point(line1: CollisionLine, line2: CollisionLine) -> tuple[float, float]:
        x1, y1 = line1.point1
        m1, l1 = line1.nap_vector
        x2, y2 = line2.point1
        m2, l2 = line2.nap_vector
        det = -m2 * l1 + m1 * l2
        if det != 0:
            det1 = -(-y1 * m1 + x1 * l1) * m2 + (-y2 * m2 + x2 * l2) * m1
            det2 = -(-y1 * m1 + x1 * l1) * l2 + (-y2 * m2 + x2 * l2) * l1
            return tuple((det1 / det, det2 / det))
        return inf, inf

    @staticmethod
    def check_collision_between_lines(line1: CollisionLine, line2: CollisionLine, gap=0.001) -> bool:
        crossing_x, crossing_y = CollisionLineChecker.get_crossing_point(line1, line2)
        if crossing_x != inf:
            if line1.x_border[0] - gap < crossing_x < line1.x_border[1] + gap and \
                    line1.y_border[0] - gap < crossing_y < line1.y_border[1] + gap and \
                    line2.x_border[0] - gap < crossing_x < line2.x_border[1] + gap and \
                    line2.y_border[0] - gap < crossing_y < line2.y_border[1] + gap:
                return True
        return False

    @staticmethod
    def check_collision_with_rect(
            line: CollisionLine,
            collision_rect_coordinates: tuple[tuple[float, float], ...]) -> bool:
        point1, point2, point3, point4 = collision_rect_coordinates
        if CollisionLineChecker.check_collision_between_lines(line, CollisionLine(point1, point2)):
            return True
        if CollisionLineChecker.check_collision_between_lines(line, CollisionLine(point2, point3)):
            return True
        if CollisionLineChecker.check_collision_between_lines(line, CollisionLine(point3, point4)):
            return True
        if CollisionLineChecker.check_collision_between_lines(line, CollisionLine(point4, point1)):
            return True
        return False


if __name__ == "__main__":
    test_line1 = CollisionLine((0, -1), (0, 2))
    test_line2 = CollisionLine((-1, 1), (1, 1))
    cr_x, cr_y = CollisionLineChecker.get_crossing_point(test_line1, test_line2)
    print(CollisionLineChecker.get_crossing_point(test_line1, test_line2))
    print(CollisionLineChecker.check_collision_between_lines(test_line1, test_line2, gap=0.001))
    print(test_line1.x_border, test_line1.y_border)
    print(test_line1.x_border[0] < cr_x < test_line1.x_border[1])
