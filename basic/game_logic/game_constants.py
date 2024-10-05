ONE_TICK_TO_PX = 100
EMPTY_CODE = '00'
CODES_TABLE = {
    "fb0": "floor_basic",
    "fb1": "floor_brick1",
    "fb2": "floor_brick2",
    "fw1": "floor_wooden1",
    "fw2": "floor_wooden2",
    "fw3": "floor_wooden3",
    "sts": "stalagmites",
    "ws1": "wall_stone1",
    "ws2": "wall_stone2",
    "ws3": "wall_stone3",
    "wdw": "window",
    "hr": "hero",
    "ky": "key",
    "ch": "chess",
    "vs": "vase",
    "mn": "money"
}
OBJECTS_SETTINGS = {
    "floor_basic": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_basic.png"]}},
    "floor_brick1": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_brick1.png"]}},
    "floor_brick2": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_brick2.png"]}},
    "floor_wooden1": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden1.png"]}},
    "floor_wooden2": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden2.png"]}},
    "floor_wooden3": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden3.png"]}},
    "stalagmites": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "stalagmites.png"]}},
    "wall_stone1": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone1.png"]}},
    "wall_stone2": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone2.png"]}},
    "wall_stone3": {"size": (1, 1), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone3.png"]}},
    "window": {"size": (2, 8), "imgs": {"base": ["data", "imgs", "game_imgs", "map", "window.png"]}},
    "hero": {
        "code": "pl", "size": (1, 1),
        "imgs": {
            "attack1": ["data", "imgs", "game_imgs", "hero", "attack", "1.png"],
            "attack2": ["data", "imgs", "game_imgs", "hero", "attack", "2.png"],
            "attack3": ["data", "imgs", "game_imgs", "hero", "attack", "3.png"],
            "attack4": ["data", "imgs", "game_imgs", "hero", "attack", "4.png"],
            "attack5": ["data", "imgs", "game_imgs", "hero", "attack", "5.png"],
            "dead1": ["data", "imgs", "game_imgs", "hero", "dead", "1.png"],
            "dead2": ["data", "imgs", "game_imgs", "hero", "dead", "2.png"],
            "dead3": ["data", "imgs", "game_imgs", "hero", "dead", "3.png"],
            "dead4": ["data", "imgs", "game_imgs", "hero", "dead", "4.png"],
            "dead5": ["data", "imgs", "game_imgs", "hero", "dead", "5.png"],
            "dead6": ["data", "imgs", "game_imgs", "hero", "dead", "6.png"],
            "run1": ["data", "imgs", "game_imgs", "hero", "run", "1.png"],
            "run2": ["data", "imgs", "game_imgs", "hero", "run", "2.png"],
            "run3": ["data", "imgs", "game_imgs", "hero", "run", "3.png"],
            "run4": ["data", "imgs", "game_imgs", "hero", "run", "4.png"],
            "run5": ["data", "imgs", "game_imgs", "hero", "run", "5.png"],
            "run6": ["data", "imgs", "game_imgs", "hero", "run", "6.png"],
            "run7": ["data", "imgs", "game_imgs", "hero", "run", "7.png"],
            "walk1": ["data", "imgs", "game_imgs", "hero", "walk", "1.png"],
            "walk2": ["data", "imgs", "game_imgs", "hero", "walk", "2.png"],
            "walk3": ["data", "imgs", "game_imgs", "hero", "walk", "3.png"],
            "walk4": ["data", "imgs", "game_imgs", "hero", "walk", "4.png"],
            "walk5": ["data", "imgs", "game_imgs", "hero", "walk", "5.png"],
            "walk6": ["data", "imgs", "game_imgs", "hero", "walk", "6.png"],
            "walk7": ["data", "imgs", "game_imgs", "hero", "walk", "7.png"],
            "walk8": ["data", "imgs", "game_imgs", "hero", "walk", "8.png"]
        }
    },
    "key": {
        "code": "ky", "size": (0.7, 0.7),
        "imgs": {
            "1": ["data", "imgs", "game_imgs", "map_objects", "key", "key1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "key", "key2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "key", "key3.png"]
        }
    },
    "chess": {
        "code": "ch", "size": (0.7, 0.7),
        "imgs": {
            "1": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess4.png"]
        }
    },
    "vase": {
        "code": "vs", "size": (0.7, 0.7),
        "imgs": {
            "1": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase4.png"]
        }
    },
    "money": {
        "code": "mn", "size": (0.7, 0.7),
        "imgs": {
            "1": ["data", "imgs", "game_imgs", "map_objects", "money", "money1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "money", "money2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "money", "money3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "money", "money4.png"],
        }
    }
}
