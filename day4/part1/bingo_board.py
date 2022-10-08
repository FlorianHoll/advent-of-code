"""Class representing a bingo board."""
import numpy as np


class BingoBoard:
    """A bingo board.

    The board can be called and keeps track of the called
    numbers and their positions.

    If the board is a 3x3 board:

    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

    Then internally, a second board is represented that keeps
    track of the called numbers. In the beginning, it is a NxN
    matrix of zeroes. If a number is called, a 1 is entered in
    the position of the called number. Suppose a 4 and 6 were
    called. The resulting internal matrix would consequently
    look like the following:

    [[0, 0, 0],
     [0, 1, 0],
     [1, 0, 0]]

    If one of the rows or columns is full (calculated via the
    row-/ column-sums), the `bingo` attribute is set to True.

    :param numbers: The numbers on a board as a np.ndarray.
        The array has to be symmetrical (i.e. N x N) and two-
        dimensional.
    """

    def __init__(self, numbers: np.ndarray) -> None:
        """Initialize the BingoBoard."""
        if not numbers.ndim == 2:
            raise ValueError(
                f"The bingo board can only have 2 dimensions, "
                f"found {numbers.ndim} dimensions."
            )
        if not numbers.shape[0] == numbers.shape[1]:
            raise ValueError(
                f"The bingo board has to be symmetrical. Found "
                f"a board with dimensions {numbers.shape}."
            )
        self.board = numbers
        # We will indicate a called number in this matrix.
        self.board_called = np.zeros_like(numbers)
        self.called_bingo = False

    def _full_row_or_column(self, axis: int) -> bool:
        """Check if there are full rows or columns.

        The check works by calculating the row-/ col-sums of the
        matrix that represents the called positions. The matrix
        has a 0 where numbers were not called and a 1 where numbers
        were called. Therefore, if a row- or column-sum is equal
        to the number of columns or rows, respectively, the row/
        column consists of all 1s, i.e. it is full.
        """
        marginal_sums = self.board_called.sum(axis=axis)
        return np.any(marginal_sums == len(marginal_sums))

    def _full_column(self) -> bool:
        return self._full_row_or_column(axis=0)

    def _full_row(self) -> bool:
        return self._full_row_or_column(axis=1)

    def _check_bingo(self) -> None:
        if self._full_row() or self._full_column():
            self.called_bingo = True

    def call_number(self, number: int) -> None:
        """Call a number, i.e. check if the number is on the board.

        If on the board, the number is marked. If a
        whole row or columns is marked, bingo is called.
        """
        if number in self.board:
            self.board_called[np.where(self.board == number)] = 1
            self._check_bingo()

    def get_sum_of_all_non_called_numbers(self):
        """Get the sum of all numbers that were not called."""
        return self.board[np.where(self.board_called == 0)].sum()
