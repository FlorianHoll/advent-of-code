"""Test the solution."""
# pylint: skip-file
from day6.part2.fish_population_part2 import FishPopulation
from day6.read_data import read_day6_data


def test_new_implementation_works():
    """Test if the solution aligns with the example."""
    test_input = [3, 4, 3, 1, 2]
    population = FishPopulation(test_input)
    [population.simulate_one_day() for _ in range(80)]
    assert population.number_of_fish == 5934


def test_new_implementation_works_for_part1():
    """Test if the solution also works for part 1 of the day.

    In part 1, we had a different implementation strategy. Since we
    know that the answer was correct, we can use this to test whether
    the new algorithm also works for the whole input data for 80 days.
    """
    puzzle_input = read_day6_data()
    population = FishPopulation(puzzle_input)
    [population.simulate_one_day() for _ in range(80)]
    assert population.number_of_fish == 355386


def test_input_for_more_days():
    """Test if the solution also alligns for more days."""
    test_input = [3, 4, 3, 1, 2]
    population = FishPopulation(test_input)
    [population.simulate_one_day() for _ in range(256)]
    assert population.number_of_fish == 26984457539
