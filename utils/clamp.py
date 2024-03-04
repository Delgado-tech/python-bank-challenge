def clamp(value: int | float, v_min: int | float, v_max: int | float):
    return min(max(value, v_min), v_max)