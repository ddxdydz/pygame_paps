DEFAULT_WINDOW_SIZE = DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT = 1300, 800
SCREEN_RESIZEABLE = True
FPS = 60

DEFAULT_TICK_SIZE = 140  # ONE TICK TO PX
DEFAULT_GGUI_SCALE_COEFFICIENT = 1  # if 1 - no scale, else coef * size
CAMERA_SPEED = 2  # WINDOWS PER SECOND in camera observed mod
MIN_PROCESSING_MOVE_DELTA = 0.01  # ticks

AUDIO_PATHS = {
    "menu": ["data", "audio", "music", "menu.mp3"],
}
IMAGE_PATHS = {
    "icon": ["data", "imgs", "icon", "icon.png"],
    "menu_background": ["data", "imgs", "menu_imgs", "menu_background.png"]
}
OTHER_PATHS = {
}

GENERAL_RULES = """
    Общее управление:
Esc: пауза с возможностью выхода в меню
Alt + Enter: переключение на полный экран
Tab: показать идикатор FPS off/on
"""
MUSIC_RULES = """
    Управление музыкой:
Space: пауза музыки
стрелки влево вправо: изменение громкости
"""
SCENE_DEBUG_RULES = """
    Общая отладка сцены:
+/-: increase/decrease tick size
O: режим свободной камеры off/on
V: show gui off/on
G: show grid off/on
R: screen autosize
P: показ визуальной информации для отладки off/on
M: отправить сообщение с параметрамы отображения
"""
