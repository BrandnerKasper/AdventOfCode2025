import pytest
from invalid_id import get_invalid_ids_part_2


@pytest.mark.parametrize("input_list, expected_output", [
    ("11-22", [11, 22]),
    ("95-115", [99, 111]),
    ("998-1012", [999, 1010]),
    ("1188511880-1188511890", [1188511885]),
    ("222220-222224", [222222]),
    ("1698522-1698528", []),
    ("446443-446449", [446446]),
    ("38593856-38593862", [38593859]),
    ("565653-565659", [565656]),
    ("824824821-824824827", [824824824]),
    ("2121212118-2121212124", [2121212121])
])


def test(input_list, expected_output):
    assert get_invalid_ids_part_2(input_list) == expected_output