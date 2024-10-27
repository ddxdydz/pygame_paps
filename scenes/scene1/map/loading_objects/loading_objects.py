from basic.general_game_logic.base_objects.GameObject import GameObject
from basic.general_game_logic.scene_folder.Scene import Scene
from basic.general_settings import EMPTY_CODE
from scenes.scene1.game_objects.Chess import Chess
from scenes.scene1.game_objects.Key import Key
from scenes.scene1.game_objects.Money import Money
from scenes.scene1.game_objects.Player import Player
from scenes.scene1.game_objects.Sceleton import Sceleton
from scenes.scene1.game_objects.Vase import Vase
from scenes.scene1.general.scene_settings import OBJECTS_VISUALISATION

class_map = {
    "chess": Chess,
    "key": Key,
    "money": Money,
    "vase": Vase,
    "hero": Player,
    "sceleton": Sceleton
}


def get_objects(scheme, parent_scene: Scene):
    game_objects = {"heroes": [], "enemies": [], "others": []}
    for row in range(len(scheme)):
        for col in range(len(scheme[0])):
            code = scheme[row][col]
            if code != EMPTY_CODE:
                width, height = OBJECTS_VISUALISATION[code]["size"]
                dx, dy = (1 - width) / 2, (1 - height) / 2  # centering
                obj = class_map[code]((col + dx, row - dy), size=(width, height), parent_scene=parent_scene)
                if code == "hero":
                    game_objects["heroes"].append(obj)
                elif code == "sceleton":
                    game_objects["enemies"].append(obj)
                else:
                    game_objects["others"].append(obj)
    return game_objects


def get_player_index(game_objects: [GameObject, ...]):
    for obj_index in range(len(game_objects)):
        obj = game_objects[obj_index]
        if isinstance(obj, Player):
            return obj_index


def get_enemy_index(game_objects: [GameObject, ...]):
    for obj_index in range(len(game_objects)):
        obj = game_objects[obj_index]
        if isinstance(obj, Sceleton):
            return obj_index


def get_player(game_objects: [GameObject, ...]):
    for obj in game_objects:
        if isinstance(obj, Player):
            return obj
