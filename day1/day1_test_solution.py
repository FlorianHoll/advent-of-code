"""Test the own solution."""
from day1.day1_part2 import find_nr_bigger_sliding_windows

# Test that sliding window size works.
test_data = [12, 23, 30, 50]
assert find_nr_bigger_sliding_windows(test_data, 4) == 0
assert find_nr_bigger_sliding_windows(test_data, 3) == 1
assert find_nr_bigger_sliding_windows(test_data, 2) == 2
assert find_nr_bigger_sliding_windows(test_data, 1) == 3

# Test with the example data.
data_from_example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
assert find_nr_bigger_sliding_windows(data_from_example) == 5
