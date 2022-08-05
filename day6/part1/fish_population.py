"""A population of fish."""
from day6.fish import Lanternfish


class FishPopulation:
    """A fish population.

    The population has all fish

    :param initial_population: The population to start with. Simply a list
        of integers that corresponds to the number of days the respective
        fish has left until reproducing.
    """

    def __init__(self, initial_population: list[int]) -> None:
        """Initialize the FishPopulation."""
        self.population = [Lanternfish(days) for days in initial_population]

    def simulate_one_day(self) -> None:
        """Simulate one day.

        If a fish reproduces, it creates a new fish that is added to a new
        list of new fish and its reproduction timer is reset. Finally, the
        lists are merged so that the new population is the old one plus the
        new fish.
        """
        new_fish = []
        for fish in self.population:
            fish.one_day_passed()
            if fish.reproduces_today:
                new_fish.append(Lanternfish(days_until_reproduction=8))
                fish.reset_reproduction_time()
        self.population += new_fish

    @property
    def number_of_fish(self) -> int:
        """Return the number of fish in the population."""
        return len(self.population)

    def show_all_days(self) -> list[int]:
        """Return the number of days left for each fish in the population."""
        return [fish.days_until_reproduction for fish in self.population]
