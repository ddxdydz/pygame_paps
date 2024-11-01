from basic.general_settings import GENERAL_RULES, MUSIC_RULES, SCENE_DEBUG_RULES

SCENE_RULES = """
    Цель игры:
найти ключ и открыть сундук в лабиринте

    Управление персонажем:
зажатые W, S, D, A: передвижение
зажатый Shift: бег
зажатое E: удар
"""
SCENE_LOCAL_DEBUG_RULES = """
    Отладка:
I: проницаемые стены off/on
T: показ таймера прохождения off/on     не работает
Y: убрать ограничение на бег off/on
U: убрать ограничение на здоровье off/on
J: получение 100000 дамага
"""

RULES = SCENE_RULES + GENERAL_RULES + MUSIC_RULES + SCENE_LOCAL_DEBUG_RULES + SCENE_DEBUG_RULES
