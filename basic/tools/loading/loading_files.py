import os
import sys

import pygame


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def join_path(path: list[str]):
    return os.path.join(*path)


def get_full_path(path: list[str]):
    return resource_path(join_path(path))


def load_image(path: list[str], size=None, convert_alpha=False, colorkey=None):
    fullname = get_full_path(path)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if size is not None:
        image = pygame.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)  # переданный ей цвет станет прозрачным
        return image.convert_alpha()

    if convert_alpha:
        return image.convert_alpha()
    return image.convert()
