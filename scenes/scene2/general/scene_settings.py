MAP_SIZE_IN_PX = 2500, 2500
OBJECTS_VISUALISATION = {
    "map_background": {"size": (20, 20), "paths": {"base": ["data", "scene2", "imgs", "map", "game_map.png"]}},
    "player": {
        "size": (1, 1), "paths": {
            "down": ["data", "scene2", "imgs", "player", "down.png"],
            "up": ["data", "scene2", "imgs", "player", "up.png"],
            "left": ["data", "scene2", "imgs", "player", "left.png"],
            "right": ["data", "scene2", "imgs", "player", "right.png"]
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
PLAYER_ANIMATION = {
    "down": {
        "frames": ["down"],
        "frames_per_second": 1, "priority": 0, "end_cycle_stage": "down", "require_reset": False
    },
    "up": {
        "frames": ["up"],
        "frames_per_second": 1, "priority": 0, "end_cycle_stage": "down", "require_reset": False
    },
    "left": {
        "frames": ["left"],
        "frames_per_second": 1, "priority": 0, "end_cycle_stage": "down", "require_reset": False
    },
    "right": {
        "frames": ["right"],
        "frames_per_second": 1, "priority": 0, "end_cycle_stage": "down", "require_reset": False
    }
}
# DOWN, UP, LEFT, RIGHT
