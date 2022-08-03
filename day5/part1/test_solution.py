"""Test the solution."""
# pylint: skip-file
from day5.part1.read_data import read_day5_data
from day5.part1.vent_map import VentMap


def test_game_works_for_example_data():
    """Test if the solution aligns with the example."""
    vent_locations = read_day5_data("day5_test_input")
    vent_map = VentMap(vent_locations)
    for positions in vent_locations:
        vent_map.update_vent_locations(positions)
    result = vent_map.count_nr_of_overlaps()
    assert result == 5
