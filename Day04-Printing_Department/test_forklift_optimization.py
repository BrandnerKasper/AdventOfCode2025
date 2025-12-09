import pytest
from forklift_optimization import turn_str_into_grid, mark, turn_grid_into_str, count_x, fork_optimization


@pytest.mark.parametrize("input_list, expected_output", [
    ("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""",
     [[0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
      [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
      [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
      [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]]),
    ("""..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""",
     [[0, 0, 2, 2, 0, 2, 2, 1, 2, 0],
      [2, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 2, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
      [2, 1, 0, 1, 1, 1, 1, 0, 1, 2],
      [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
      [2, 0, 1, 1, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [2, 0, 2, 0, 1, 1, 1, 0, 2, 0]])
])
def test_str_into_grid(input_list, expected_output):
    assert turn_str_into_grid(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ([[0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
      [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
      [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
      [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]],

     [[0, 0, 2, 2, 0, 2, 2, 1, 2, 0],
      [2, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 2, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
      [2, 1, 0, 1, 1, 1, 1, 0, 1, 2],
      [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
      [2, 0, 1, 1, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [2, 0, 2, 0, 1, 1, 1, 0, 2, 0]])
])
def test_forklift_marker(input_list, expected_output):
    assert mark(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ([[0, 0, 2, 2, 0, 2, 2, 1, 2, 0],
      [2, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 2, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
      [2, 1, 0, 1, 1, 1, 1, 0, 1, 2],
      [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
      [2, 0, 1, 1, 1, 0, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [2, 0, 2, 0, 1, 1, 1, 0, 2, 0]],
     """..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""")
])
def test_forklift_marker(input_list, expected_output):
    assert turn_grid_into_str(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("""..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""", 13)
])
def test_count_x(input_list, expected_output):
    assert count_x(input_list) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""", 13)
])
def test_fork_optimization(input_list, expected_output):
    assert fork_optimization(input_list) == expected_output