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
        self.difference_vector = np.abs(self.vector_2 - self.vector_1)

    @property
    def _is_horizontal_or_vertical_line(self):
        return 0 in self.difference_vector

    def get_vector_of_positions(self) -> Union[np.ndarray, None]:
        """Get the vector of the positions."""
        if self._is_horizontal_or_vertical_line:
            return self._get_vector()

        return None

    def _get_vector(self) -> np.ndarray:
        """Get the final vector of the vents."""
        non_zeros = self.difference_vector[self.difference_vector != 0]
        difference_length = int(np.unique(non_zeros))
        x1, x2 = self.x_coordinates
        y1, y2 = self.y_coordinates
        x_vector = np.linspace(x1, x2, difference_length + 1).astype(int)
        y_vector = np.linspace(y1, y2, difference_length + 1).astype(int)
        vector = np.c_[x_vector, y_vector]

        return vector


class AdvancedVentLocation(VentLocation):
    """A vent location that also allows for diagonal vent positions."""

    @property
    def _is_diagonal_line(self):
        return len(np.unique(self.difference_vector)) == 1

    def get_vector_of_positions(self) -> Union[np.ndarray, None]:
        """Get the vector of positions."""
        if self._is_horizontal_or_vertical_line or self._is_diagonal_line:
            return self._get_vector()

        return None
