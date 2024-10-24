import os
import sys

import pygame


def join_path(path: list[str, ...]):
    return os.path.join(*path)


def load_image(path: list[str, ...], size=None, colorkey=None):
    fullname = os.path.join(*path)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)  # переданный ей цвет станет прозрачным

    if size is not None:
        image = pygame.transform.scale(image, size)

    return image
