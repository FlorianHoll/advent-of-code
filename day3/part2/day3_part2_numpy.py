"""Day 3, part 2. Implementation in numpy.

Next, you should verify the life support rating, which can be determined by
multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that
can be found in your diagnostic report - finding them is the tricky part.
Both values are located using a similar process that involves filtering out
values until only one remains. Before searching for either rating value, start
with the full list of binary numbers from your diagnostic report and consider
just the first bit of those numbers. Then:

    Keep only numbers selected by the bit criteria for the type of rating value
        for which you are searching. Discard numbers which do not match the bit
        criteria.
    If you only have one number left, stop; this is the rating value for which
        you are searching.
    Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1)
        in the current bit position, and keep only numbers with that bit in
        that position. If 0 and 1 are equally common, keep values with a 1
        in the position being considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1)
        in the current bit position, and keep only numbers with that bit in
        that position. If 0 and 1 are equally common, keep values with a 0
        in the position being considered.

For example, to determine the oxygen generator rating value using the same
example diagnostic report from above:

    Start with all 12 numbers and consider only the first bit of each number.
        There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers
        with a 1 in the first position:
        11110, 10110, 10111, 10101, 11100, 10000, and 11001.
    Then, consider the second bit of the 7 remaining numbers: there are more
        0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in
        the second position: 10110, 10111, 10101, and 10000.
    In the third position, three of the four numbers have a 1,
        so keep those three: 10110, 10111, and 10101.
    In the fourth position, two of the three numbers have a 1,
        so keep those two: 10110 and 10111.
    In the fifth position, there are an equal number of 0 bits and 1 bits
        (one each). So, to find the oxygen generator rating,
        keep the number with a 1 in that position: 10111.
    As there is only one number left, stop; the oxygen generator
        rating is 10111, or 23 in decimal.

Then, to determine the CO2 scrubber rating value from the same example above:

    Start again with all 12 numbers and consider only the first bit of each number.
        There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers
        with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
    Then, consider the second bit of the 5 remaining numbers: there are fewer 1
        bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the
        second position: 01111 and 01010.
    In the third position, there are an equal number of 0 bits and 1 bits
        (one each). So, to find the CO2 scrubber rating, keep the number
        with a 0 in that position: 01010.
    As there is only one number left, stop; the CO2 scrubber rating
        is 01010, or 10 in decimal.

Finally, to find the life support rating, multiply the oxygen generator rating (23)
by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator
rating and CO2 scrubber rating, then multiply them together.

What is the life support rating of the submarine?
(Be sure to represent your answer in decimal, not binary.)
"""
import numpy as np

from day3.day3_part1_numpy import index_vertically
from day3.day3_part1_numpy import list_to_binary_string
from day3.day3_part1_numpy import read_data


class BitCriterionChooser:
    """Choose based on the bit criterion.

    :param data: The data, pre-processed as vertically indexed data, i.e. an
        array with two dimensions where the rows contains one binary number
        per row and each column represents the bits in that vertical position.
        Each cell of the array therefore corresponds to one bit (as an integer).
    :param criterion: "most" or "least"; if "most", the most common bit is
        searched and chosen; if "least", the least common bit is searched and
        chosen.
    """

    def __init__(self, data: np.ndarray, criterion: str = "most") -> None:
        """Initialize the BitCriterionChooser."""
        self.data = data
        self.original_data = data.copy()
        self.criterion_most_common = criterion == "most"

    @property
    def _finished(self):
        """Return indicator if the choosing process is finished.

        According to the instruction, the process stops if there is
        only row left. Therefore, we simply check whether this is true.
        """
        return self.data.shape[0] == 1

    @staticmethod
    def _invert_bits(bits: np.ndarray) -> np.ndarray:
        """Invert bits (1 -> 0; 0 -> 1)."""
        return np.abs(bits - 1)

    def _find_all_rows_with_bit(self, vertical_index: int, bit: int) -> None:
        """Find all rows for which the bit is its value.

        According to the instruction, in each step, only those rows
        are supposed to be kept that include the bit of interest. In
        the function, those rows are indexed. Then, the data is
        overwritten so that only the rows with the bit of interest
        at that particular index remain.

        :param vertical_index: The column to search through. Equals
            the iteration of the algorithm.
        :param bit: The bit of interest: Shall all rows that have a
            1 at the position be kept or those with a 0 at the position.
        """
        indezes = self.data[:, vertical_index] == bit
        self.data = self.data[indezes, :]

    def _find_most_or_least_common_bit(self, index):
        """Find either the most or least common bit in a specific column.

        Since there are only ones and zeros in the array, one can calculate
        the mean. If the mean is > .5, there are more 1s than 0s; therefore,
        the most common bit is 1. When representing the boolean value of the
        comparison (mean > .5) as an integer, we have the solution.

        :param index: The index, i.e. the column, to look at.
        :return: The most common bit, if the criterion is "most common";
            the least common bit otherwise.
        """
        data = self.data[:, index]
        most_common_bit = (data.mean() >= 0.5).astype(int)
        if not self.criterion_most_common:
            result = self._invert_bits(most_common_bit)
        else:
            result = most_common_bit
        return result

    def calculate_rating(self) -> int:
        """Calculate the rating.

        This is done by first checking if the stop criterion is reached;
        if not, the most or least common bit for the current index, i.e.
        the current column, is found. Then, only the rows containing that
        exact bit at that index (i.e. in that column) are kept and the
        algorithm repeats. This happens until only one row is left.

        :return: The resulting row as a decimal number.
        """
        index = 0
        while not self._finished:
            bit = self._find_most_or_least_common_bit(index)
            self._find_all_rows_with_bit(index, bit)
            index += 1
        binary_number = list_to_binary_string(self.data.flatten())
        return int(binary_number, 2)


if __name__ == "__main__":
    data = read_data()
    vertical_data = index_vertically(data)
    oxygen_rating = BitCriterionChooser(vertical_data).calculate_rating()
    co2_rating = BitCriterionChooser(
        vertical_data, criterion="least"
    ).calculate_rating()
    print(f"The result is: {oxygen_rating * co2_rating}.")
