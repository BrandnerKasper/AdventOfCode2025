import pytest
from joltage_bank import calculate_highest_joltage


@pytest.mark.parametrize("input_list, expected_output", [
    ("987654321111111", 98),
    ("811111111111119", 89),
    ("234234234234278", 78),
    ("818181911112111", 92)
])


def test(input_list, expected_output):
    assert calculate_highest_joltage(input_list, 2) == expected_output