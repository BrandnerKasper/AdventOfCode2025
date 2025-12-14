import pytest
from cephalopod_math import do_homework


@pytest.mark.parametrize("input_list, expected_output", [
    ("123 328  51 64\n45 64  387 23\n6 98  215 314\n*   +   *   +", 4277556),
])
def test_count_fresh_ingredients(input_list, expected_output):
    assert do_homework(input_list) == expected_output