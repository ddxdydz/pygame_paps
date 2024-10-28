def get_surface_size_by_screen_proportions(
        surface_size: tuple[int, int], screen_size: tuple[int, int]) -> tuple[int, int]:
    surface_width, surface_height = surface_size
    screen_width, screen_height = screen_size

    surface_proportions = surface_width / surface_height
    screen_proportions = screen_width / screen_height

    if surface_proportions < screen_proportions:  # main side - width
        new_surface_width = screen_width
        new_surface_height = int(surface_height * (screen_width / surface_width))
    else:  # main side - height
        new_surface_width = int(surface_width * (screen_height / surface_height))
        new_surface_height = screen_height

    return new_surface_width, new_surface_height
