"""Read in the data for day 5."""
import numpy as np


def read_day5_data(input_file: str):
    """Read the data for day5.

    The .txt file is a little more complicated: First, there are some
    numbers that represent the numbers to draw; then, there are blocks
    of numbers that represent the bingo boards.
    In order to use them, the blocks have to be split first; then,
    the blocks are indexed and formatted.
    """
    with open(f"../../data/{input_file}", "r") as txt:
        instructions = txt.read()

    # Format vent locations.
    instructions = instructions.replace("\n", ",").replace(" -> ", ",").split(",")

    # Remove empty values that result due to linebreaks.
    instructions = [int(st) for st in instructions if st.isnumeric()]
    nr_instructions = len(instructions) // (2 * 2)  # instructions are all 2 x 2.

    # Reshape to be equally sized coordinate arrays.
    vent_data = np.array(instructions).reshape((nr_instructions, 2, 2))
    return vent_data
