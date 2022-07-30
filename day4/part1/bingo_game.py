"""Class that represents a game of bingo."""
import numpy as np

from day4.part1.bingo_board import BingoBoard


class BingoGame:
    """A bingo game.

    The game consists of a number of bingo boards. For each number,
    the number is called for each board. If some board has a bingo
    after a number, the winner is returned along with the last called
    number.

    :param bingo_boards: The bingo boards as a list of np.ndarray
        where each array represents one bingo board.
    :param numbers_drawn: The drawn numbers as a 1-dimensional array.
    """

    def __init__(
        self, bingo_boards: list[np.ndarray], numbers_drawn: np.ndarray
    ) -> None:
        """Initialize the bingo game."""
        self.bingo_boards = []
        for bingo_board in bingo_boards:
            self.bingo_boards.append(BingoBoard(bingo_board))
        self.numbers_to_draw = numbers_drawn
        self.winner = None

    def _someone_has_bingo(self) -> bool:
        """Search through all boards and return whether someone called bingo."""
        return any(board.called_bingo for board in self.bingo_boards)

    def _get_winner(self) -> BingoBoard:
        """Get the one who called bingo."""
        winner_index = [board.called_bingo for board in self.bingo_boards].index(True)
        return self.bingo_boards[winner_index]

    def play(self) -> tuple[BingoBoard, int]:
        """Play the game.

        Once the game is started, the numbers are called one after another.
        After each number, it is checked is someone called bingo. If someone
        did call bingo, the winner is returned along with the last number.
        """
        while True:
            for number in self.numbers_to_draw:
                [board.call_number(number) for board in self.bingo_boards]
                if self._someone_has_bingo():
                    break
            break

        winner = self._get_winner()
        return winner, number
