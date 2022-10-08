"""Lanternfish class."""


class Lanternfish:
    """A lanternfish.

    The instruction says that the fish reproduces once the
    reproduction timer runs out. However, once a fish has
    reproduced, it has a different timer than a newly created
    fish; therefore, the easiest way to model this is with a
    class and the "days_until_reproduction" attribute.

    :param days_until_reproduction: The initial days until
        reproduction, i.e. the puzzle input or "8" if it is
        a newly created fish.
    """

    def __init__(self, days_until_reproduction: int) -> None:
        """Initialize the lanternfish."""
        self.days_until_reproduction = days_until_reproduction

    def one_day_passed(self) -> None:
        """Pass one day, i.e. decrease the days attribute by 1."""
        self.days_until_reproduction -= 1

    @property
    def reproduces_today(self) -> bool:
        """Indicate if the fish reproduces today.

        On the day that days_until_reproduction == 0, the
        fish does NOT reproduce yet - it is only on the following
        day that it reproduces. Therefore, we check if the days
        are smaller than 0.
        """
        return self.days_until_reproduction < 0

    def reset_reproduction_time(self) -> None:
        """Reset the reproduction timer according to the instructions."""
        self.days_until_reproduction = 6
