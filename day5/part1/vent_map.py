"""A vent map that represents the location of the vents."""
import numpy as np

from day5.part1.vent_location import VentLocation


class VentMap:
    """Represent the locations of the vents."""

    def __init__(self, vent_locations: np.ndarray) -> None:
        """Initialize the VentMap."""
        map_size = np.repeat(vent_locations.max() + 1, 2)
        self.map = np.zeros(map_size).astype(int)

    def update_vent_locations(self, vent_location: np.ndarray) -> None:
        """Upda the vent location."""
        coordinates = VentLocation(vent_location).get_vector_of_positions()
        if coordinates is not None:
            x1, x2, y1, y2 = coordinates
            self.map[x1:x2, y1:y2] += 1

    def count_nr_of_overlaps(self) -> int:
        """Count the number of overlapping vents.

        Since vents overlap as soon as there is more than one vent
        in one position, all positions with more than one vent are
        summed up.
        """
        return (self.map > 1).sum()
