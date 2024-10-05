from typing import Iterable


class DrawConverting:
    @staticmethod
    def main_to_draw_coordinates(point, camera_coordinates, one_tick_to_px) -> tuple[int, int]:
        x0, y0 = camera_coordinates
        xm, ym = point
        return (xm - x0) * one_tick_to_px, -(ym - y0) * one_tick_to_px

    @staticmethod
    def draw_to_main_coordinates(point, camera_coordinates, one_tick_to_px) -> tuple[int, int]:
        x0, y0 = camera_coordinates
        xc, yc = point
        return xc / one_tick_to_px + x0, - yc / one_tick_to_px + y0

    @staticmethod
    def get_primitive_draw_coordinates(primitive, camera_coordinates, one_tick_to_px):
        result_primitive = []
        for point in primitive:
            result_primitive.append(
                DrawConverting.main_to_draw_coordinates(
                    point, camera_coordinates, one_tick_to_px
                )
            )
        return result_primitive
