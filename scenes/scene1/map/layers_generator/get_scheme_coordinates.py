from math import trunc


def get_scheme_coordinates(centre_coordinates):
    x, y = centre_coordinates
    col, row = trunc(x), trunc(y) + 1
    return row, col
