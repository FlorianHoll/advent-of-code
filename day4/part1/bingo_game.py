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

    def _game_is_finished(self) -> bool:
        """Set the finish condition of the game.

        Since the condition differs from part1 of day4 to the
        second task, this method has to be implemented by the
        children classes.
        """
        pass

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
                # Sorting out the finished boards becomes important in the
                #   second part of the assignment.
                self._sort_out_finished_boards()

                # Call all boards.
                [board.call_number(number) for board in self.bingo_boards]

                if self._game_is_finished():
                    break
            break

        winner = self._get_winner()
        return winner, number

    def _sort_out_finished_boards(self):
        """Sort out the finished boards.

        This is important for the second part of the puzzle. Here,
        we need the last board to win. Sorting out all finished
        boards is the easiest method to do find this board.
        """
        self.bingo_boards = [
            board for board in self.bingo_boards if not board.called_bingo
        ]


class FirstOneWinsBingoGame(BingoGame):
    """A bingo game where the first player to call bingo ends the game."""

    def _game_is_finished(self) -> bool:
        return self._someone_has_bingo()

    def _someone_has_bingo(self) -> bool:
        """Search through all boards and return whether someone called bingo."""
        return any(board.called_bingo for board in self.bingo_boards)


class LastOneWinsBingoGame(BingoGame):
    """A bingo game where the last player to call bingo ends the game."""

    def _game_is_finished(self) -> bool:
        return self._everyone_has_bingo()

    def _everyone_has_bingo(self) -> bool:
        """Search through all boards and return whether everyone called bingo."""
        return all(board.called_bingo for board in self.bingo_boards)
