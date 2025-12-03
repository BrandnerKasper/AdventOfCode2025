import pytest
from invalid_id import get_invalid_ids


@pytest.mark.parametrize("input_list, expected_output", [
    ("11-22", [11, 22]),
    ("95-115", [99]),
    ("998-1012", [1010]),
    ("1188511880-1188511890", [1188511885]),
    ("222220-222224", [222222]),
    ("1698522-1698528", []),
    ("446443-446449", [446446]),
    ("38593856-38593862", [38593859])
])


def test(input_list, expected_output):
    assert get_invalid_ids(input_list) == expected_output