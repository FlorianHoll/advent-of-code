"""Find the minimum possible fuel spent."""
import numpy as np


def find_minimum_fuel_spent(initial_positions=np.ndarray) -> tuple[int, int]:
    """Find the minimum fuel spent.

    Since the amount of fuel spent is simply the difference between
    two points (moving from 16 to 2 = 14 fuel spent), this can be
    done as an element-wise matrix subtraction.
    The subtraction matrix is a NxM matrix where
        - N is the maximum that occurs in the initial positions.
        - M is the length of the vector, i.e. the number of fish.
    The rows represent the different possible numbers (ranging
    from 0 to the maximum number found in the initial positions).
    The columns represent the number of fish, so that we obtain
    the amount spent for each fish when doing the element-wise
    subtraction.

    Consider the following example:
    If the initial fish positions are: [4, 2, 2, 1], then the resulting
    subtraction matrix will be:
    [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

    When subtracting the initial fish position by the subtraction matrix,
    the result is:
    [[ 4,  2,  2,  1],
     [ 3,  1,  1,  0],
     [ 2,  0,  0, -1],
     [ 1, -1, -1, -2],
     [ 0, -2, -2, -3]]

    The absolute values of these numbers are taken (because fuel
    consumption can only be positive) and the row sums are calculated.
    These represent the combined amount of fuel spent if the fish
    align at position 0, 1, 2, etc., respectively.

    Therefore, the result (the row sums) is:
    [9, 5, 3, 5, 7].

    Therefore, at index 2, the amount of fuel spent is minimal (with
    a total of 3 units of fuel spent). Therefore, the solution would
    be to align the fish at position 2 for a combined fuel spent of 3.
    """
    initial_positions = np.array(initial_positions)
    max_pos = int(initial_positions.max())
    nr_pos = len(initial_positions)

    subtraction_matrix = np.repeat(np.arange(max_pos), nr_pos).reshape(max_pos, nr_pos)
    subtraction_result = np.abs(initial_positions - subtraction_matrix).sum(axis=1)

    position_to_align_fish_at = subtraction_result.argmin()
    amount_of_fuel_spent = subtraction_result.min()
    return position_to_align_fish_at, amount_of_fuel_spent
