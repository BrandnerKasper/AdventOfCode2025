import pytest
from invalid_id import get_invalid_ids, sum_invalid_ids


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
def test_get_invalid_ids_part_1(input_list, expected_output):
    assert get_invalid_ids(input_list, True) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862", 1227775554)
])
def test_sum_invalid_ids_part_1(input_list, expected_output):
    id_ranges = input_list.split(",")
    assert sum_invalid_ids(id_ranges, True) == expected_output


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
def test_get_invalid_ids_part_2(input_list, expected_output):
    assert get_invalid_ids(input_list, False) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124", 4174379265)
])
def test_sum_invalid_ids_part_2(input_list, expected_output):
    id_ranges = input_list.split(",")
    assert sum_invalid_ids(id_ranges, False) == expected_output