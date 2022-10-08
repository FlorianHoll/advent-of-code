"""Test the own solution."""
from day2.day2_part1 import find_final_coordinates
from day2.day2_part2 import find_final_coordinates_with_aim

# Test with the example data.
data_from_example = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
assert find_final_coordinates(data_from_example) == tuple([15, 10])
assert find_final_coordinates_with_aim(data_from_example) == tuple([15, 60])
