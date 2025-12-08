import pytest
from dial import dial


@pytest.mark.parametrize("input_list, expected_output", [
    (["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"], 3)
])
def test_dial_count_exact_zero(input_list, expected_output):
    assert dial(input_list, True) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    (["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"], 6),
    (["L500", "R500"], 10)
])
def test_dial_count_zero(input_list, expected_output):
    assert dial(input_list, False) == expected_output