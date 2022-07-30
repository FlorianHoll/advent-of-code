"""Test the solution."""
# pylint: skip-file
import numpy as np

from day4.part1.bingo_game import LastOneWinsBingoGame

EXAMPLE_NUMBERS_TO_DRAW = np.array(
    [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
)

EXAMPLE_BOARDS = [
    np.array(
        [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
    ).reshape(5, 5),
    np.array(
        [
            3,
            15,
            0,
            2,
            22,
            9,
            18,
            13,
            17,
            5,
            19,
            8,
            7,
            25,
            23,
            20,
            11,
            10,
            24,
            4,
            14,
            21,
            16,
            12,
            6,
        ]
    ).reshape(5, 5),
    np.array(
        [
            14,
            21,
            17,
            24,
            4,
            10,
            16,
            15,
            9,
            19,
            18,
            8,
            23,
            26,
            20,
            22,
            11,
            13,
            6,
            5,
            2,
            0,
            12,
            3,
            7,
        ]
    ).reshape(5, 5),
]


def test_game_works_for_example_data():
    """Test if the solution aligns with the example."""
    game = LastOneWinsBingoGame(EXAMPLE_BOARDS, EXAMPLE_NUMBERS_TO_DRAW)
    winner, last_number = game.play()
    assert last_number == 13
    assert winner.get_sum_of_all_non_called_numbers() == 148
