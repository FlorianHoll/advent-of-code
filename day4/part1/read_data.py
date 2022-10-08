"""Read in the data."""
import numpy as np


def read_day4_data():
    """Read the data.

    The .txt file is a little more complicated: First, there are some
    numbers that represent the numbers to draw; then, there are blocks
    of numbers that represent the bingo boards.
    In order to use them, the blocks have to be split first; then,
    the blocks are indexed and formatted.
    """
    with open("../../data/day4_input.txt", "r") as txt:
        instructions = txt.read()
    # Find the position where the numbers end and the bingo boards begin.
    separation = instructions.find("\n\n")

    # Index and format the numbers.
    numbers_to_draw = instructions[:separation]
    numbers_to_draw = numbers_to_draw.split(",")
    numbers_to_draw = np.array(numbers_to_draw).astype(int)

    # Index and format bingo boards.
    bingo_boards = (
        instructions[separation:]  # index all boards
        .replace(" ", ",")  # separate the numbers
        .replace("\n", ",")  # remove the line breaks
        .split(",")
    )
    # Remove empty values that result due to linebreaks.
    bingo_boards = [number for number in bingo_boards if number.isnumeric()]
    nr_bingo_boards = len(bingo_boards) // (5 * 5)  # boards are all 5x5.

    # Reshape to be equally sized 5x5 bingo boards.
    bingo_boards = np.array(bingo_boards).astype(int).reshape((nr_bingo_boards, 5, 5))
    return bingo_boards, numbers_to_draw


if __name__ == "__main__":
    bingo, numbers = read_day4_data()
    assert bingo.shape[-2:] == (5, 5)
    assert numbers.ndim == 1
