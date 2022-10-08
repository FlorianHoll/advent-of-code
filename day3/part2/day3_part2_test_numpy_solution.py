"""Test the numpy based solution of day3, part 2."""
import numpy as np

from day3.part1.day3_part1_numpy import index_vertically
from day3.part2.day3_part2_numpy import BitCriterionChooser

example_data = np.array(
    [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
)


def test_example_data_returns_expected_result():
    """Test if the class returns the correct result for the example data."""
    vertical_data = index_vertically(example_data)
    most_common_strategy = BitCriterionChooser(vertical_data).calculate_rating()
    least_common_strategy = BitCriterionChooser(
        vertical_data, "least"
    ).calculate_rating()
    assert most_common_strategy == 23
    assert least_common_strategy == 10
