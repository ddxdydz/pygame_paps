MAP_SIZE_IN_PX = 2500, 2500
OBJECTS_VISUALISATION = {
    "map_background": {"size": (20, 20), "paths": {"base": ["data", "scene2", "imgs", "map", "game_map.jpg"]}},
    "player": {
        "size": (1, 1), "convert_alpha": True, "paths": {
            "down": ["data", "scene2", "imgs", "player", "down.png"],
            "up": ["data", "scene2", "imgs", "player", "up.png"],
            "left": ["data", "scene2", "imgs", "player", "left.png"],
            "right": ["data", "scene2", "imgs", "player", "right.png"],
            "death": ["data", "scene2", "imgs", "player", "death.png"],
            "hit": ["data", "scene2", "imgs", "player", "hit.png"]
        }
    },
    "shadow": {
        "size": (1, 1), "convert_alpha": True, "paths": {
            "shadow": ["data", "scene2", "imgs", "enemy", "shadow.png"],
            "hit": ["data", "scene2", "imgs", "enemy", "hit.png"],
            "death": ["data", "scene2", "imgs", "enemy", "death.png"]
        }
    }
}
RECT_BORDERS = """
140, 860, 137, 905;
173, 1764, 332, 184;
469, 1845, 488, 192;
54, 384, 406, 484;
360, 438, 1981, 286;
2238, 575, 235, 714;
921, 1408, 656, 629;
1252, 1194, 1132, 305;
"""
LINE_BORDERS = """
266,867;157,1172;125,1239;105,1317;131,1387;164,1408;232,1513;206,1613;228,1681;240,1719;314,1807;471,1813;665,1919;685,1965;749,1981;937,1904;919,1788;996,1625;1100,1574;1211,1444;1453,1250;1573,1261;1586,1286;1711,1282;1771,1322;1813,1319;1982,1252;2074,1200;2149,1208;2287,1215;2435,1041;2391,1026;2312,1021;2304,957;1666,855;1404,806;1388,818;1557,861;1912,859;2170,859;2231,909;2329,948;2402,931;2380,799;2224,671;1646,639;1532,606;1484,593;1468,500;1177,481;965,407;851,431;668,488;414,606;401,712;393,751;391,791;266,853;
"""
SCENE_AUDIO_PATHS = {
    "lose": ["data", "audio", "sound", "lose.wav"],
    "coin": ["data", "audio", "sound", "coin.wav"],
    "win": ["data", "audio", "sound", "win.wav"],
    "achievement": ["data", "audio", "sound", "achievement.wav"],
    "death": ["data", "audio", "sound", "death_sound.wav"],
    "sceleton_lose": ["data", "audio", "sound", "sceleton_lose.wav"],
    "sceleton_hit": ["data", "audio", "sound", "sceleton_hit.wav"],
    "hero_hit": ["data", "audio", "sound", "hero_hit.wav"],
    "sceleton_alert": ["data", "audio", "sound", "sceleton_alert.wav"],
    "notification": ["data", "audio", "sound", "notification.wav"]
}
GAME_GUI_IMAGES = {
    "health_bar": {"convert_alpha": True, "paths": {"base": ["data", "imgs", "game_imgs", "other", "health_bar.png"]}},
    "stamina_bar": {"convert_alpha": True, "paths": {"base": ["data", "imgs", "game_imgs", "other", "stamina_bar.png"]}}
}
PLAYER_ANIMATION = {
    "attack": {
        "frames": ["down"],
        "frames_per_second": 1, "priority": 1, "end_cycle_stage": "stay", "require_reset": True
    },
    "stay": {
        "frames": ["down"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "stay", "require_reset": False
    },
    "dying": {
        "frames": ["hit"],
        "frames_per_second": 5, "priority": 3, "end_cycle_stage": "death", "require_reset": True
    },
    "death": {
        "frames": ["death"],
        "frames_per_second": 1, "priority": 4, "end_cycle_stage": "death", "require_reset": False
    },
    "walk_down": {
        "frames": ["down"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "walk_down", "require_reset": False
    },
    "walk_up": {
        "frames": ["up"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "walk_up", "require_reset": False
    },
    "walk_left": {
        "frames": ["left"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "walk_left", "require_reset": False
    },
    "walk_right": {
        "frames": ["right"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "walk_right", "require_reset": False
    },
    "run_down": {
        "frames": ["down"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "run_down", "require_reset": False
    },
    "run_up": {
        "frames": ["up"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "run_up", "require_reset": False
    },
    "run_left": {
        "frames": ["left"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "run_left", "require_reset": False
    },
    "run_right": {
        "frames": ["right"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "run_right", "require_reset": False
    },
    "hit": {
        "frames": ["down", "hit", "down"],
        "frames_per_second": 3, "priority": 2, "end_cycle_stage": "stay", "require_reset": True
    }
}
# ATTACK, STAY, DYING, DEATH, WALK_DOWN, WALK_UP, WALK_LEFT, WALK_RIGHT, RUN_DOWN, RUN_UP, RUN_LEFT, RUN_RIGHT, HIT
SHADOW_ANIMATION = {
    "attack": {
        "frames": ["shadow"],
        "frames_per_second": 1, "priority": 1, "end_cycle_stage": "stay", "require_reset": True
    },
    "stay": {
        "frames": ["shadow"],
        "frames_per_second": 6, "priority": 0, "end_cycle_stage": "stay", "require_reset": False
    },
    "dying": {
        "frames": ["shadow", "death"],
        "frames_per_second": 4, "priority": 4, "end_cycle_stage": "death", "require_reset": True
    },
    "death": {
        "frames": ["death"],
        "frames_per_second": 3, "priority": 5, "end_cycle_stage": "death", "require_reset": False
    },
    "walk": {
        "frames": ["shadow"],
        "frames_per_second": 16, "priority": 0, "end_cycle_stage": "walk", "require_reset": False
    },
    "hit": {
        "frames": ["hit", "hit", "hit", "hit", "hit", "hit"],
        "frames_per_second": 10, "priority": 3, "end_cycle_stage": "stay", "require_reset": True
    },
    "react": {
        "frames": ["shadow"],
        "frames_per_second": 2, "priority": 2, "end_cycle_stage": "stay", "require_reset": True
    }
}
