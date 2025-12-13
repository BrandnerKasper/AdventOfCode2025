import pytest
from fresh_ingredients import fresh, count_fresh_ingredients, get_fresh_ingredients_ids, count_fresh_ingredients_ids, get_fresh_ingredients_ids_efficient, count_fresh_ingredients_ids_efficient


@pytest.mark.parametrize("input_list, expected_output", [
    (("3-5\n10-14\n16-20\n12-18", "1"), False),
    (("3-5\n10-14\n16-20\n12-18", "5"), True),
    (("3-5\n10-14\n16-20\n12-18", "8"), False),
    (("3-5\n10-14\n16-20\n12-18", "11"), True),
    (("3-5\n10-14\n16-20\n12-18", "17"), True),
    (("3-5\n10-14\n16-20\n12-18", "32"), False),
])
def test_fresh(input_list, expected_output):
    id_ranges = input_list[0]
    food_id = input_list[1]
    assert fresh(id_ranges, food_id) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32", 3),
])
def test_count_fresh_ingredients(input_list, expected_output):
    assert count_fresh_ingredients(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("3-5\n10-14\n16-20\n12-18", [3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
])
def test_get_fresh_ingredients_ids(input_list, expected_output):
    assert get_fresh_ingredients_ids_efficient(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32", 14),
])
def test_count_fresh_ingredients_ids(input_list, expected_output):
    assert count_fresh_ingredients_ids_efficient(input_list) == expected_output
