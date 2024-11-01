EMPTY_CODE = "00"  # For maze processing
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
    "game": ["data", "audio", "music", "game.mp3"],
    "notification": ["data", "audio", "sound", "notification.wav"]
}
GAME_GUI_IMAGES = {
    "health_bar": {"paths": {"base": ["data", "imgs", "game_imgs", "other", "health_bar.png"]}},
    "stamina_bar": {"paths": {"base": ["data", "imgs", "game_imgs", "other", "stamina_bar.png"]}}
}
OBJECTS_VISUALISATION = {
    "floor_basic": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_basic.png"]}},
    "floor_brick1": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_brick1.png"]}},
    "floor_brick2": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_brick2.png"]}},
    "floor_wooden1": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden1.png"]}},
    "floor_wooden2": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden2.png"]}},
    "floor_wooden3": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "floor_wooden3.png"]}},
    "stalagmites": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "stalagmites.png"]}},
    "wall_stone1": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone1.png"]}},
    "wall_stone2": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone2.png"]}},
    "wall_stone3": {"size": (1, 1), "paths": {"base": ["data", "imgs", "game_imgs", "map", "wall_stone3.png"]}},
    "window": {"size": (2, 8), "paths": {"base": ["data", "imgs", "game_imgs", "map", "window.png"]}},
    "hero": {
        "size": (1, 1),
        "paths": {
            "base": ["data", "imgs", "game_imgs", "hero", "attack", "1.png"],
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
            "walk8": ["data", "imgs", "game_imgs", "hero", "walk", "8.png"],
            "hit1": ["data", "imgs", "game_imgs", "hero", "hit", "1.png"],
            "hit2": ["data", "imgs", "game_imgs", "hero", "hit", "2.png"],
        }
    },
    "key": {
        "size": (0.7, 0.7),
        "paths": {
            "base": ["data", "imgs", "game_imgs", "map_objects", "key", "key1.png"],
            "1": ["data", "imgs", "game_imgs", "map_objects", "key", "key1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "key", "key2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "key", "key3.png"]
        }
    },
    "chess": {
        "size": (0.7, 0.7),
        "paths": {
            "base": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess1.png"],
            "1": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "chess", "chess4.png"]
        }
    },
    "vase": {
        "size": (0.7, 0.7),
        "paths": {
            "base": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase1.png"],
            "1": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "vase", "vase4.png"]
        }
    },
    "money": {
        "size": (0.7, 0.7),
        "paths": {
            "base": ["data", "imgs", "game_imgs", "map_objects", "money", "money1.png"],
            "1": ["data", "imgs", "game_imgs", "map_objects", "money", "money1.png"],
            "2": ["data", "imgs", "game_imgs", "map_objects", "money", "money2.png"],
            "3": ["data", "imgs", "game_imgs", "map_objects", "money", "money3.png"],
            "4": ["data", "imgs", "game_imgs", "map_objects", "money", "money4.png"],
        }
    },
    "sceleton": {
        "size": (0.7, 0.7),
        "paths": {
            "attack1": ["data", "imgs", "game_imgs", "skeleton", "attack", "1.png"],
            "attack2": ["data", "imgs", "game_imgs", "skeleton", "attack", "2.png"],
            "attack3": ["data", "imgs", "game_imgs", "skeleton", "attack", "3.png"],
            "attack4": ["data", "imgs", "game_imgs", "skeleton", "attack", "4.png"],
            "attack5": ["data", "imgs", "game_imgs", "skeleton", "attack", "5.png"],
            "attack6": ["data", "imgs", "game_imgs", "skeleton", "attack", "6.png"],
            "attack7": ["data", "imgs", "game_imgs", "skeleton", "attack", "7.png"],
            "attack8": ["data", "imgs", "game_imgs", "skeleton", "attack", "8.png"],
            "attack9": ["data", "imgs", "game_imgs", "skeleton", "attack", "9.png"],
            "attack10": ["data", "imgs", "game_imgs", "skeleton", "attack", "10.png"],
            "attack11": ["data", "imgs", "game_imgs", "skeleton", "attack", "11.png"],
            "attack12": ["data", "imgs", "game_imgs", "skeleton", "attack", "12.png"],
            "attack13": ["data", "imgs", "game_imgs", "skeleton", "attack", "13.png"],
            "attack14": ["data", "imgs", "game_imgs", "skeleton", "attack", "14.png"],
            "attack15": ["data", "imgs", "game_imgs", "skeleton", "attack", "15.png"],
            "attack16": ["data", "imgs", "game_imgs", "skeleton", "attack", "16.png"],
            "attack17": ["data", "imgs", "game_imgs", "skeleton", "attack", "17.png"],
            "attack18": ["data", "imgs", "game_imgs", "skeleton", "attack", "18.png"],
            "dead1": ["data", "imgs", "game_imgs", "skeleton",  "dead", "1.png"],
            "dead2": ["data", "imgs", "game_imgs", "skeleton",  "dead", "2.png"],
            "dead3": ["data", "imgs", "game_imgs", "skeleton",  "dead", "3.png"],
            "dead4": ["data", "imgs", "game_imgs", "skeleton",  "dead", "4.png"],
            "dead5": ["data", "imgs", "game_imgs", "skeleton",  "dead", "5.png"],
            "dead6": ["data", "imgs", "game_imgs", "skeleton",  "dead", "6.png"],
            "dead7": ["data", "imgs", "game_imgs", "skeleton",  "dead", "7.png"],
            "dead8": ["data", "imgs", "game_imgs", "skeleton",  "dead", "8.png"],
            "dead9": ["data", "imgs", "game_imgs", "skeleton",  "dead", "9.png"],
            "dead10": ["data", "imgs", "game_imgs", "skeleton", "dead", "10.png"],
            "dead11": ["data", "imgs", "game_imgs", "skeleton", "dead", "11.png"],
            "dead12": ["data", "imgs", "game_imgs", "skeleton", "dead", "12.png"],
            "dead13": ["data", "imgs", "game_imgs", "skeleton", "dead", "13.png"],
            "dead14": ["data", "imgs", "game_imgs", "skeleton", "dead", "14.png"],
            "dead15": ["data", "imgs", "game_imgs", "skeleton", "dead", "15.png"],
            "hit1": ["data", "imgs", "game_imgs", "skeleton",  "hit", "1.png"],
            "hit2": ["data", "imgs", "game_imgs", "skeleton",  "hit", "2.png"],
            "hit3": ["data", "imgs", "game_imgs", "skeleton",  "hit", "3.png"],
            "hit4": ["data", "imgs", "game_imgs", "skeleton",  "hit", "4.png"],
            "hit5": ["data", "imgs", "game_imgs", "skeleton",  "hit", "5.png"],
            "hit6": ["data", "imgs", "game_imgs", "skeleton",  "hit", "6.png"],
            "hit7": ["data", "imgs", "game_imgs", "skeleton",  "hit", "7.png"],
            "hit8": ["data", "imgs", "game_imgs", "skeleton",  "hit", "8.png"],
            "idle1": ["data", "imgs", "game_imgs", "skeleton",  "idle", "1.png"],
            "idle2": ["data", "imgs", "game_imgs", "skeleton",  "idle", "2.png"],
            "idle3": ["data", "imgs", "game_imgs", "skeleton",  "idle", "3.png"],
            "idle4": ["data", "imgs", "game_imgs", "skeleton",  "idle", "4.png"],
            "idle5": ["data", "imgs", "game_imgs", "skeleton",  "idle", "5.png"],
            "idle6": ["data", "imgs", "game_imgs", "skeleton",  "idle", "6.png"],
            "idle7": ["data", "imgs", "game_imgs", "skeleton",  "idle", "7.png"],
            "idle8": ["data", "imgs", "game_imgs", "skeleton",  "idle", "8.png"],
            "idle9": ["data", "imgs", "game_imgs", "skeleton",  "idle", "9.png"],
            "idle10": ["data", "imgs", "game_imgs", "skeleton", "idle", "10.png"],
            "idle11": ["data", "imgs", "game_imgs", "skeleton", "idle", "11.png"],
            "react1": ["data", "imgs", "game_imgs", "skeleton",  "react", "1.png"],
            "react2": ["data", "imgs", "game_imgs", "skeleton",  "react", "2.png"],
            "react3": ["data", "imgs", "game_imgs", "skeleton",  "react", "3.png"],
            "react4": ["data", "imgs", "game_imgs", "skeleton",  "react", "4.png"],
            "walk1": ["data", "imgs", "game_imgs", "skeleton",  "walk", "1.png"],
            "walk2": ["data", "imgs", "game_imgs", "skeleton",  "walk", "2.png"],
            "walk3": ["data", "imgs", "game_imgs", "skeleton",  "walk", "3.png"],
            "walk4": ["data", "imgs", "game_imgs", "skeleton",  "walk", "4.png"],
            "walk5": ["data", "imgs", "game_imgs", "skeleton",  "walk", "5.png"],
            "walk6": ["data", "imgs", "game_imgs", "skeleton",  "walk", "6.png"],
            "walk7": ["data", "imgs", "game_imgs", "skeleton",  "walk", "7.png"],
            "walk8": ["data", "imgs", "game_imgs", "skeleton",  "walk", "8.png"],
            "walk9": ["data", "imgs", "game_imgs", "skeleton",  "walk", "9.png"],
            "walk10": ["data", "imgs", "game_imgs", "skeleton", "walk", "10.png"],
            "walk11": ["data", "imgs", "game_imgs", "skeleton", "walk", "11.png"],
            "walk12": ["data", "imgs", "game_imgs", "skeleton", "walk", "12.png"],
            "walk13": ["data", "imgs", "game_imgs", "skeleton", "walk", "13.png"],
        }
    }
}
PLAYER_ANIMATION = {
    "attack": {
        "frames": ["attack1", "attack2", "attack3", "attack4", "attack5", "attack4"],
        "frames_per_second": 8, "priority": 1, "end_cycle_stage": "stay", "require_reset": True
    },
    "stay": {
        "frames": ["attack1"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "stay", "require_reset": False
    },
    "dying": {
        "frames": ["hit2", "dead1", "dead2", "dead3", "dead4", "dead5", "dead6"],
        "frames_per_second": 5, "priority": 3, "end_cycle_stage": "death", "require_reset": True
    },
    "death": {
        "frames": ["dead6"],
        "frames_per_second": 1, "priority": 4, "end_cycle_stage": "death", "require_reset": False
    },
    "walk": {
        "frames": ["walk1", "walk2", "walk3", "walk4", "walk5"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "walk", "require_reset": False
    },
    "run": {
        "frames": ["run1", "run2", "run3", "run4", "run5", "run6", "run7"],
        "frames_per_second": 5, "priority": 0, "end_cycle_stage": "run", "require_reset": False
    },
    "hit": {
        "frames": ["hit1", "hit2", "hit1"],
        "frames_per_second": 4, "priority": 2, "end_cycle_stage": "stay", "require_reset": True
    }
}
SCELETON_ANIMATION = {
    "attack": {
        "frames": ["attack1", "attack2", "attack3", "attack4", "attack5",
                   "attack6", "attack7", "attack8", "attack9", "attack10", "attack11", "attack12"],
        "frames_per_second": 12, "priority": 1, "end_cycle_stage": "stay", "require_reset": True
    },
    "stay": {
        "frames": ["idle1", "idle2", "idle3", "idle4", "idle5", "idle6", "idle7", "idle8", "idle9", "idle10", "idle11"],
        "frames_per_second": 6, "priority": 0, "end_cycle_stage": "stay", "require_reset": False
    },
    "dying": {
        "frames": ["dead1", "dead2", "dead3", "dead4", "dead5", "dead6", "dead7", "dead8", "dead9",
                   "dead10", "dead11", "dead12", "dead13", "dead14", "dead15"],
        "frames_per_second": 4, "priority": 4, "end_cycle_stage": "death", "require_reset": True
    },
    "death": {
        "frames": ["dead15"],
        "frames_per_second": 3, "priority": 5, "end_cycle_stage": "death", "require_reset": False
    },
    "walk": {
        "frames": ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6", "walk7", "walk8",
                   "walk9", "walk10", "walk11", "walk12", "walk13"],
        "frames_per_second": 16, "priority": 0, "end_cycle_stage": "walk", "require_reset": False
    },
    "hit": {
        "frames": ["hit1", "hit2", "hit3", "hit4", "hit5", "hit6", "hit7", "hit8"],
        "frames_per_second": 10, "priority": 3, "end_cycle_stage": "stay", "require_reset": True
    },
    "react": {
        "frames": ["react1", "react2", "react3", "react4", "react1", "react2", "react3", "react4"],
        "frames_per_second": 2, "priority": 2, "end_cycle_stage": "stay", "require_reset": True
    }
}
