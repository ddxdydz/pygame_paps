DEFAULT_WINDOW_SIZE = DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT = 1300, 800
FPS = 60

DEFAULT_TICK_SIZE = 140  # ONE TICK TO PX
ONE_GGUI_TICK_TO_PX = 100
CAMERA_SPEED = 2  # WINDOWS PER SECOND
MIN_PROCESSING_MOVE_DELTA = 0.01  # ticks
EMPTY_CODE = "00"

AUDIO_PATHS = {
    "menu": ["data", "audio", "music", "menu.mp3"],
    "game": ["data", "audio", "music", "game.mp3"],
    "notification": ["data", "audio", "sound", "notification.wav"]
}
IMAGE_PATHS = {
    "icon": ["data", "imgs", "icon", "icon.png"],
    "audio_on": ["data", "imgs", "audio_imgs", "audioon.png"],
    "audio_off": ["data", "imgs", "audio_imgs", "audiooff.png"],
    "menu_background": ["data", "imgs", "menu_imgs", "menu_background.png"]
}
OTHER_PATHS = {
    "rules": ["data", "rules.txt"]
}

"""
Hot keys:
    alt + enter     fullscreen toggle
    <-  ->          music valume
    space           music pause
Scene debugger hot keys:
    +               increase tick size
    -               decrease tick size
    o	enable free camera
    v	show gui
    p	show debug info
    t	show timer
    m	send message with size
"""
