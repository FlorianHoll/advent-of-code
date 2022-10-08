"""Read in the data for day 7."""
import numpy as np


def read_day7_data():
    """Read the data for day 7."""
    with open("../../data/day7_input.txt", "r") as txt:
        positions = txt.read()
    return np.array(positions.strip().split(",")).astype(int)
