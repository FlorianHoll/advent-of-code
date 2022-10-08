"""A fish population.

This time, we need to implement the fish populaton differently because
implementing an object-oriented approach becomes to slow due to the
exponential growth that is inherent to the problem. Therefore, we need
a more elegant approach to model the fish growth.
"""
import numpy as np


class FishPopulation:
    """A fish population.

    :param initial_population: The initial population, given as a list
        of integers which represent the number of days left until
        reproduction.
    """

    def __init__(self, initial_population: list[int]) -> None:
        """Initialize the FishPopulation.

        The implementation differs this time: We have an array that counts
        the number of the fish who have a specific amount of days left until
        reproduction. Suppose the input list of fish with their days is
        [6, 4, 3, 1, 2, 0, 1, 2, 0, 7, 0].
        Then the resulting population array would consist of the number of
        fish for each day:

        days_left  = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        population = [3, 2, 2, 1, 0, 0, 1, 1, 0]

        When thinking about the population as a dictionary object, the
        days left are the keys and the population array would be the values.
        The keys correspond to the index, which makes it easier to index
        later on.
        """
        indezes, counts = np.unique(initial_population, return_counts=True)
        self.population = np.zeros(9)
        self.population[indezes] = counts

    def simulate_one_day(self):
        """Simulate on day.

        Since the population array represents the number of fish with
        i number of days left at index i, we can use this. The passing
        of one day can be thought of as shifting the array one index
        "to the left". This is because all fish that have 0 days left
        will create a new fish, i.e. their number equals the number of
        new fish; thus, they can be thought as moving from the first
        index of the array (0) to the last (8).
        However, the shifting of index 0 to index 8 only represents
        the NEW fish; the fish that reproduced to get the new fish
        now again have 6 days left until reproduction. Therefore, their
        number [now at the last position in the array] has to be added
        to the number of fish with 6 days left (i.e. added to the fish
        in index position 6).
        Consider this example:

        Population before the passing of the day:
        [5, 1, 2, 6, 3, 5, 2, 3, 9, 2]

        Birth of the new fish:
           [1, 2, 6, 3, 5, 2, 3, 9, 2, 5]

        Reset of the fish that give birth
        [1, 2, 6, 3, 5, 2, 3, 9+5, 2, 5]

        Therefore, the final population after the day is:
        [1, 2, 6, 3, 5, 2, 3, 14, 2, 5]
        """
        # The "roll" command shifts the whole array to the left by x
        #   steps in the specified direction.
        self.population = np.roll(self.population, -1)

        # Add the fish that reproduced to the ones with 6 days left.
        self.population[6] += self.population[-1]

    @property
    def number_of_fish(self):
        """Return the number of fish in the population.

        Since the population array already consists of the number of
        fish for a specific day, all that needs to be done is to sum
        up the fish.
        """
        return int(self.population.sum())
