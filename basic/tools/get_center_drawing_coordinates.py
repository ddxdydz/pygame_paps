def get_center_drawing_coordinates(screen, text_surface):
    width, height = text_surface.get_size()
    x = (screen.get_width() - width) // 2
    y = (screen.get_height() - height) // 2
    return x, y
