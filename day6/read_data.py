"""Read in the data for day 6."""
import numpy as np


def read_day6_data():
    """Read the data for day 6."""
    with open("../../data/day6_input.txt", "r") as txt:
        instructions = txt.read()

    # Remove empty values that result due to linebreaks.
    instructions = [int(st) for st in instructions.split(",") if st.isnumeric()]

    return np.array(instructions)


if __name__ == "__main__":
    result = read_day6_data()
