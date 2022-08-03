"""A class representing the location of a hydrothermal vent."""
from typing import Union

import numpy as np


class VentLocation:
    """A vent lcation."""

    def __init__(self, locations: np.ndarray) -> None:
        """Initialize the VentLocation."""
        if locations.shape != (2, 2):
            raise ValueError("Arrays have to be coordinate pairs of shape 2x2.")
        self.locations = locations

    def _index_location(self, axis: int, position: int) -> np.ndarray:
        if axis == 0:
            points = self.locations[:, position]
        else:
            points = self.locations[position, :]
        return points

    def _check_for_line(self, axis: int, position: int) -> bool:
        points = self._index_location(axis, position)
        return len(np.unique(points)) == 1

    @staticmethod
    def _reverse_position(position: int):
        return np.abs(position - 1)

    def get_vector_of_positions(self) -> Union[np.ndarray, None]:
        """Get the vector of the positions."""
        for position in range(len(self.locations)):
            for axis in [0, 1]:
                if self._check_for_line(axis, position):
                    if not self._check_for_line(axis, self._reverse_position(position)):
                        return self._get_final_indices(axis, position)

        return None

    def _get_final_indices(self, axis: int, position: int) -> np.ndarray:
        """Get the final indices of the vents."""
        stationary_point = np.unique(self._index_location(axis, position))
        stationary_point = np.r_[stationary_point, stationary_point]

        non_stationary_points = self._index_location(
            axis, self._reverse_position(position)
        )
        # Points have to be sorted to be able to index properly.
        non_stationary_points.sort()
        # add one to be able to index properly
        non_stationary_points[1] += 1
        stationary_point[1] += 1

        point_indices = (
            np.r_[non_stationary_points, stationary_point]
            if position == 0
            else np.r_[stationary_point, non_stationary_points]
        )

        return point_indices


#
# if __name__ == "__main__":
#     t = np.array([[578, 391], [578, 322]])
#     result = VentLocation(t).get_vector_of_positions()
