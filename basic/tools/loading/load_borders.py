from basic.general_game_logic.collision_system.lines_collision.CollisionLine import CollisionLine
from basic.general_game_logic.game_visualization.GameVisualizer import GameVisualizer
from scenes.scene1.game_objects.Wall import Wall


def point_px_to_main(
        x_px: int, y_px: int,
        main_size: tuple[float, float],
        px_size: tuple[int, int]) -> tuple[float, float]:
    width, height = main_size
    width_px, height_px = px_size
    return x_px * width / width_px, (height_px - y_px) * height / height_px - 1


def point_on_screen_to_px(
        img_pos: tuple[int, int], game_visualizer: GameVisualizer,
        main_size: tuple[float, float],
        map_size_in_px: tuple[int, int]) -> tuple[int, int]:
    xm, ym = game_visualizer.to_main_coordinates(*img_pos)
    width_px, height_px = map_size_in_px
    width, height = main_size
    x_px = int(xm * width_px / width)
    y_px = int(-(ym + 1) * height_px / height + height_px)
    return x_px, y_px


def size_px_to_main(
        input_width: int, input_height: int,
        main_size: tuple[float, float],
        px_size: tuple[int, int]) -> tuple[float, float]:
    width, height = main_size
    width_px, height_px = px_size
    return input_width * width / width_px, input_height * height / height_px


def load_rect_border(data: str, map_size, map_size_in_px) -> list[Wall]:
    result = []

    for border_str in data.split(";"):
        striped_str = border_str.strip()
        if striped_str:
            border = [int(val) for val in border_str.split(",")]
            border[0], border[1] = point_px_to_main(border[0], border[1], map_size, map_size_in_px)
            border[2], border[3] = size_px_to_main(border[2], border[3], map_size, map_size_in_px)
            result.append(Wall((border[0], border[1]), (border[2], border[3])))

    return result


def load_line_border(data: str, map_size, map_size_in_px) -> list[CollisionLine]:
    points = []
    for border_str in data.split(";"):
        striped_str = border_str.strip()
        if striped_str:
            point = [int(val) for val in border_str.split(",")]
            points.append(point_px_to_main(*point, map_size, map_size_in_px))

    if len(points) < 2:
        raise Exception("load_line_border: len(points) < 2")

    result = []
    for point_index in range(1, len(points)):
        last_point_index = point_index - 1
        result.append(CollisionLine(points[point_index], points[last_point_index]))

    return result
