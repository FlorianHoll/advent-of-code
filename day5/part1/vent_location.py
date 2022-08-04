"""A class representing the location of a hydrothermal vent."""
from typing import Union

import numpy as np


class VentLocation:
    """A vent lcation."""

    def __init__(self, locations: np.ndarray) -> None:
        """Initialize the VentLocation."""
        if locations.shape != (2, 2):
            raise ValueError("Arrays have to be coordinate pairs of shape 2x2.")
        self.vector_1, self.vector_2 = locations
        self.x_coordinates = locations[:, 0]
        self.y_coordinates = locations[:, 1]
        self.difference_vector = self.vector_2 - self.vector_1

    def get_vector_of_positions(self) -> Union[np.ndarray, None]:
        """Get the vector of the positions."""
        if 0 in self.difference_vector:
            return self._get_final_indices()

        return None

    def _get_final_indices(self) -> np.ndarray:
        """Get the final indices of the vents."""
        self.x_coordinates.sort()
        self.x_coordinates[1] += 1
        self.y_coordinates.sort()
        self.y_coordinates[1] += 1

        return np.r_[self.x_coordinates, self.y_coordinates]
