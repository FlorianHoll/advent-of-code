"""Test the solution."""
# pylint: skip-file
from day6.fish_population import FishPopulation


def test_new_fish_logic_works():
    """Test if the logic for creating new fish works."""
    test_input = [0]
    population = FishPopulation(test_input)
    population.simulate_one_day()
    result = population.show_all_days()
    assert result == [6, 8]


def test_game_works_for_example_data():
    """Test if the solution aligns with the example."""
    test_input = [3, 4, 3, 1, 2]
    population = FishPopulation(test_input)
    for day in range(80):
        population.simulate_one_day()
        if day == 0:
            assert population.show_all_days() == [2, 3, 2, 0, 1]
        if day == 1:
            assert population.show_all_days() == [1, 2, 1, 6, 0, 8]
        if day == 2:
            assert population.show_all_days() == [0, 1, 0, 5, 6, 7, 8]
    result = population.number_of_fish
    assert result == 5934
