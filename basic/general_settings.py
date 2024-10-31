DEFAULT_WINDOW_SIZE = DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT = 1300, 800
SCREEN_RESIZEABLE = True
FPS = 60

DEFAULT_TICK_SIZE = 140  # ONE TICK TO PX
DEFAULT_GGUI_SCALE_COEFFICIENT = 1  # if 1 - no scale, else coef * size
CAMERA_SPEED = 2  # WINDOWS PER SECOND in camera observed mod
MIN_PROCESSING_MOVE_DELTA = 0.01  # ticks

AUDIO_PATHS = {
    "menu": ["data", "audio", "music", "menu.mp3"],
    "game": ["data", "audio", "music", "game.mp3"],
    "notification": ["data", "audio", "sound", "notification.wav"]
}
IMAGE_PATHS = {
    "icon": ["data", "imgs", "icon", "icon.png"],
    "menu_background": ["data", "imgs", "menu_imgs", "menu_background.png"]
}
OTHER_PATHS = {
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
    g   show grid
    r   auto size
    p	show debug info
    m	send message with size
"""
