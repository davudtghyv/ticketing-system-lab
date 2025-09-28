def celsius_to_fahrenheit(c: float) -> float:
    """
    Convert Celsius to Fahrenheit using F = C * 9/5 + 32.
    """
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("c must be a numeric type (int or float)")
    return c * 9 / 5 + 32