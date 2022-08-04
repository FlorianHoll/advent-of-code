"""Test the solution."""
# pylint: skip-file
import numpy as np
import pytest

from day5.read_data import read_day5_data
from day5.vent_location import AdvancedVentLocation
from day5.vent_map import VentMap


@pytest.mark.parametrize(
    "vent_locations, expected_result",
    [
        (np.array([[0, 0], [7, 7]]), True),
        (np.array([[0, 2], [5, 7]]), True),
        (np.array([[9, 7], [7, 9]]), True),
        (np.array([[9, 7], [5, 3]]), True),
        (np.array([[7, 9], [4, 6]]), True),
        (np.array([[7, 9], [6, 5]]), False),
        (np.array([[7, 9], [6, 1]]), False),
        (np.array([[0, 5], [5, 5]]), False),
    ],
)
def test_diagonal_lines_are_recognized(vent_locations, expected_result):
    """Test if diagonal lines are recognized."""
    result = AdvancedVentLocation(vent_locations)._is_diagonal_line
    assert result == expected_result


def test_game_works_for_example_data():
    """Test if the solution aligns with the example."""
    expected_map = np.array(
        [
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
            [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
            [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
            [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
        ]
    )
    vent_locations = read_day5_data("day5_test_input.txt")
    vent_map = VentMap(vent_locations)
    for positions in vent_locations:
        vent_map.update_vent_locations(positions, allow_diagonals=True)
    assert np.all(vent_map.map.T == expected_map)

    result = vent_map.count_nr_of_overlaps()
    assert result == 12
