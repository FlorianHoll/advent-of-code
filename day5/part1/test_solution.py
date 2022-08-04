"""Test the solution."""
# pylint: skip-file
import numpy as np

from day5.read_data import read_day5_data
from day5.vent_map import VentMap


def test_game_works_for_example_data():
    """Test if the solution aligns with the example."""
    expected_map = np.array(
        [
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            [
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
            ],
            [
                0,
                1,
                1,
                2,
                1,
                1,
                1,
                2,
                1,
                1,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                2,
                2,
                2,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
            ],
        ]
    )
    vent_locations = read_day5_data("day5_test_input.txt")
    vent_map = VentMap(vent_locations)
    for positions in vent_locations:
        vent_map.update_vent_locations(positions)
    assert np.all(vent_map.map.T == expected_map)

    result = vent_map.count_nr_of_overlaps()
    assert result == 5
