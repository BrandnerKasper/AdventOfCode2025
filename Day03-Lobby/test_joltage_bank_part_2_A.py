import pytest
@pytest.mark.parametrize("input_list, expected_output", [
    ("987654321111111", 987654321111),
    ("811111111111119", 811111111119),
    ("234234234234278", 434234234278),
    ("818181911112111", 888911112111)
])


def test(input_list, expected_output):
    assert calculate_highest_joltage(input_list, 12) == expected_output


from joltage_bank import calculate_highest_joltage