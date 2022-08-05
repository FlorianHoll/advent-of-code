"""Day 6, part 2.

Suppose the lanternfish live forever and have unlimited food and space.
Would they take over the entire ocean?

After 256 days in the example above, there would be a total of
26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""
from day6.part2.fish_population_part2 import FishPopulation
from day6.read_data import read_day6_data

if __name__ == "__main__":
    initial_population = read_day6_data()
    population = FishPopulation(initial_population)
    [population.simulate_one_day() for _ in range(256)]
    result = population.number_of_fish
    print(f"Number of fish after 256 days: {result}")
