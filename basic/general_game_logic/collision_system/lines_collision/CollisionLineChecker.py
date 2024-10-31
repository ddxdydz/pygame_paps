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
    def check_collision_between_lines(line1: CollisionLine, line2: CollisionLine, seg=0.01) -> bool:
        crossing_x, crossing_y = CollisionLineChecker.get_crossing_point(line1, line2)
        if crossing_x != inf:
            if line1.x_border[0] - seg < crossing_x < line1.x_border[1] + seg and \
                    line1.y_border[0] - seg < crossing_y < line1.y_border[1] + seg and \
                    line2.x_border[0] - seg < crossing_x < line2.x_border[1] + seg and \
                    line2.y_border[0] - seg < crossing_y < line2.y_border[1] + seg:
                return True
        return False

    @staticmethod
    def check_collision_with_rect(
            line: CollisionLine,
            collision_rect_coordinates: tuple[tuple[float, float], ...]) -> bool:
        point1, point2, point3, point4 = collision_rect_coordinates
        rect_line1, rect_line2 = CollisionLine(point1, point3), CollisionLine(point2, point4)
        if CollisionLineChecker.check_collision_between_lines(line, rect_line1):
            return True
        if CollisionLineChecker.check_collision_between_lines(line, rect_line2):
            return True
        return False
