def get_dynamic_alpha(time_showing, time_start_decrease_alpha, current_time, default_visibility: int) -> int:
    if current_time - time_start_decrease_alpha < 0:
        delta = time_showing - time_start_decrease_alpha
        return int(default_visibility * (current_time / delta))
    else:
        return default_visibility
