import pytest
from invalid_id import sum_invalid_ids_part_1


@pytest.mark.parametrize("input_list, expected_output", [
    ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862", 1227775554)
])


def test(input_list, expected_output):
    id_ranges = input_list.split(",")
    assert sum_invalid_ids_part_1(id_ranges) == expected_output