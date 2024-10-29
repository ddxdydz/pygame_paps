from basic.tools.loading.loading_files import join_path
from scenes.scene1.game_objects.Wall import Wall
from scenes.scene2.general.scene_settings import OTHER_PATHS, MAP_SIZE_IN_PX


def load_borders(map_size):
    result = []
    width, height = map_size
    width_px, height_px = MAP_SIZE_IN_PX
    with open(join_path(OTHER_PATHS["borders"]), mode='rt', encoding='UTF-8') as file:
        for border_str in file.readlines():
            border = [int(val) for val in border_str.split(",")]
            border[0] = border[0] * width / width_px
            border[1] = (height_px - border[1]) * height / height_px - 1
            border[2] = border[2] * width / width_px
            border[3] = border[3] * height / height_px
            result.append(Wall((border[0], border[1]), (border[2], border[3])))
    return result
