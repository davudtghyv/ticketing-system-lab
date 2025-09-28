import math
import pytest
from src.temperature import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32

def test_positive_integer():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_integer():
    assert celsius_to_fahrenheit(-40) == -40

def test_float_precision():
    result = celsius_to_fahrenheit(36.6)
    assert math.isclose(result, 97.88, rel_tol=1e-9, abs_tol=1e-12)

@pytest.mark.parametrize("c, expected", [
    (1.5, 34.7),
    (-10.5, 13.1),
    (25.0, 77.0),
])
def test_parametrized(c, expected):
    assert math.isclose(celsius_to_fahrenheit(c), expected, rel_tol=1e-9, abs_tol=1e-12)

def test_type_error_for_str():
    import pytest
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("20")