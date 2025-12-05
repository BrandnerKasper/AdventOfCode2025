import pytest
from ex01 import dial


@pytest.mark.parametrize("input_list, expected_output", [
    (["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"], 3)
])


def test(input_list, expected_output):
    assert dial(input_list) == expected_output

