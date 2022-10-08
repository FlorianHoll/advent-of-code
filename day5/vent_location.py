"""A class representing the location of a hydrothermal vent."""
from typing import Union

import numpy as np


class VentLocation:
    """A vent location.

    The class outputs a vector of all coordinates that the vent
    covers. It can do so for horizontal and vertical lines.

    :param locations: The locations as a 2x2 array where
        locations[:, 0] are the x-coordinates and locations[:, 1]
        are the y-coordinates.
    """

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
        """Indicate if the location vector is a horizontal or vertical line.

        A vector is horizontal or vertical if
        """
        return 0 in self.difference_vector

    def get_vector_of_positions(self) -> Union[np.ndarray, None]:
        """Get the vector of the vent positions."""
        if self._is_horizontal_or_vertical_line:
            return self._get_vector()

        return None

    def _get_vector(self) -> np.ndarray:
        """Get the final vector of the vents.

        We want a list that contains all the coordinates that the vent
        covers. E.g. for (1, 2) -> (1, 4), we want a resulting list that
        looks like this:
        [[1, 2],
         [1, 3],
         [1, 4]]
        In order to do this, we use the np.linspace() function to create
        an array with even spaces in between the elements. In our case,
        the space between the elements is 1 if the coordinates change
        and 0 if they do not; thus, the result is a list as described above.
        """
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
        """Get the vector of positions.

        Since now we also need to identify diagonal lines, we have to return the
        coordinates if the vector is a horizontal, vertical, or diagonal line.
        """
        if self._is_horizontal_or_vertical_line or self._is_diagonal_line:
            return self._get_vector()

        return None
