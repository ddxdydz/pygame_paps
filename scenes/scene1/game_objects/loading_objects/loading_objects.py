from basic.game_logic.GameObject import GameObject
from basic.game_logic.game_constants import EMPTY_CODE, CODES_TABLE, OBJECTS_SETTINGS
from scenes.scene1.game_objects.Chess import Chess
from scenes.scene1.game_objects.Key import Key
from scenes.scene1.game_objects.Money import Money
from scenes.scene1.game_objects.Sceleton import Sceleton
from scenes.scene1.game_objects.Vase import Vase
from scenes.scene1.game_objects.Player import Player


def get_objects(scheme) -> [GameObject, ...]:
    game_objects = []
    for row in range(len(scheme)):
        for col in range(len(scheme[0])):
            code = scheme[row][col]
            if code != EMPTY_CODE:
                if code == Chess.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    dx, dy = (1 - width) / 2, (1 - height) / 2  # centering
                    game_objects.append(Chess((col + dx, row - dy), size=(width, height)))
                elif code == Key.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    dx, dy = (1 - width) / 2, (1 - height) / 2
                    game_objects.append(Key((col + dx, row - dy), size=(width, height)))
                elif code == Money.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    dx, dy = (1 - width) / 2, (1 - height) / 2
                    game_objects.append(Money((col + dx, row - dy), size=(width, height)))
                elif code == Vase.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    dx, dy = (1 - width) / 2, (1 - height) / 2
                    game_objects.append(Vase((col + dx, row - dy), size=(width, height)))
                elif code == Player.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    player = Player((col, row), size=(width, height))
                    game_objects.append(player)
                elif code == Sceleton.CODE:
                    width, height = OBJECTS_SETTINGS[CODES_TABLE[code]]["size"]
                    dx, dy = (1 - width) / 2, (1 - height) / 2
                    game_objects.append(Sceleton((col + dx, row - dy), size=(width, height)))
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
