import pytest
from joltage_bank import calculate_highest_joltage, sum_joltage_banks


@pytest.mark.parametrize("input_list, expected_output", [
    ("987654321111111", 98),
    ("811111111111119", 89),
    ("234234234234278", 78),
    ("818181911112111", 92)
])


def test_calculate_highest_joltage_2_digits(input_list, expected_output):
    assert calculate_highest_joltage(input_list, 2) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    (["987654321111111", "811111111111119", "234234234234278", "818181911112111"], 357)
])


def test_sum_joltage_banks_2_digits(input_list, expected_output):
    assert sum_joltage_banks(input_list, 2) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("987654321111111", 987654321111),
    ("811111111111119", 811111111119),
    ("234234234234278", 434234234278),
    ("818181911112111", 888911112111)
])


def test_calculate_highest_joltage_12_digits(input_list, expected_output):
    assert calculate_highest_joltage(input_list, 12) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    (["987654321111111", "811111111111119", "234234234234278", "818181911112111"], 3121910778619)
])


def test_sum_joltage_banks_12_digits(input_list, expected_output):
    assert sum_joltage_banks(input_list, 12) == expected_output