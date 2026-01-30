import pytest
from utils import cube, fifth_power, square

# Test suite for math utility functions

def test_square():
    """Verify square calculation for various inputs."""
    assert square(2) == 4
    assert square(3) == 9
    assert square(-4) == 16
    assert square(0) == 0

def test_cube():
    """Verify cube calculation for various inputs."""
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(-3) == -27
    assert cube(0) == 0

def test_fifth_power():
    """Verify fifth power calculation for various inputs."""
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(-2) == -32
    assert fifth_power(0) == 0

def test_invalid_input():
    """Ensure functions raise TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        # We expect this to fail or raise TypeError if not handled
        # In simple Python, it might just raise TypeError on the operation
        square("string")
