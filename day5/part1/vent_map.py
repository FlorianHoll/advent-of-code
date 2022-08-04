"""A vent map that represents the location of the vents."""
import numpy as np

import day5.part1.vent_location as vl


class VentMap:
    """Represent the locations of the vents."""

    def __init__(self, vent_locations: np.ndarray) -> None:
        """Initialize the VentMap.

        A map of zeros is initialized - this map will iteratively be
        filled up with ones as we get to know the positions of the
        hydrothermal vents.
        """
        map_size = np.repeat(vent_locations.max() + 1, 2)
        self.map = np.zeros(map_size).astype(int)

    def update_vent_locations(
        self, vent_location: np.ndarray, allow_diagonals: bool = False
    ) -> None:
        """Update the vent location.

        The vector of all positions that the vent stretches from and to
        is retrieved with the help of the VentLocation class. Then, for
        each coordinate pair, the value 1 is added to the internal map
        to represent the presence of a vent in this position.
        The usage of a for-loop rather than a vectorized version is due
        to the fact that diagonal lines (part 2 of the day) cannot be
        indexed with a vector, i.e. self.map[1:8, 1:8] result in a
        different array than self.map[1, 1], self.map[2, 2], ...,
        self.map[8, 8].
        """
        vl_class_name = "AdvancedVentLocation" if allow_diagonals else "VentLocation"
        vl_class = getattr(vl, vl_class_name)
        coordinates = vl_class(vent_location).get_vector_of_positions()
        if coordinates is not None:
            for coordinate_pair in coordinates:
                x, y = coordinate_pair
                self.map[x, y] += 1

    def count_nr_of_overlaps(self) -> int:
        """Count the number of overlapping vents.

        Since vents overlap as soon as there is more than one vent
        in one position, all positions with more than one vent are
        summed up.
        """
        return (self.map > 1).sum()
