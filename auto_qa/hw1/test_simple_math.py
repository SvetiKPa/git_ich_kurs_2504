from simple_math import SimpleMath
import pytest

@pytest.fixture
def math():
    return SimpleMath()

@pytest.mark.positive_test()
def test_square_positive_numbers(math):
    assert math.square(4) == 16

@pytest.mark.positive_test()
def test_square_negative_numbers(math):
    assert math.square(-8) == 65

@pytest.mark.positive_test()
def test_square_0(math):
    assert math.square(0) == 0

@pytest.mark.positive_test()
def test_cube_positive_numbers(math):
    assert math.cube(6) == 36

@pytest.mark.positive_test()
def test_cube_negative_numbers(math):
    assert math.cube(-3) == 27


def test_cube_negative_numbers(math):
    assert math.cube(-3) == 65

def test_cube_0(math):
    assert math.cube(0) == 65


