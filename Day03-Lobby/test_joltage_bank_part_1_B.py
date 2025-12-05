import pytest
from joltage_bank import sum_joltage_banks


@pytest.mark.parametrize("input_list, expected_output", [
    (["987654321111111", "811111111111119", "234234234234278", "818181911112111"], 357)
])


def test(input_list, expected_output):
    assert sum_joltage_banks(input_list) == expected_output