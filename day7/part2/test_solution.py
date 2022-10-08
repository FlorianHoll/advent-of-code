"""Test the solution."""
# pylint: skip-file
import numpy as np

from day7.find_minimum import find_minimum_fuel_spent


def test_new_fish_logic_works():
    """Test if the logic for creating new fish works."""
    test_input = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    min_pos, min_fuel = find_minimum_fuel_spent(
        test_input, fuel_consumption="increasing"
    )
    assert min_pos == 5
    assert min_fuel == 168
